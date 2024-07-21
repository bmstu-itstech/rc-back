from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rs_back.core.models import ImageBaseModel


class Achievement(ImageBaseModel):
    """!
    @brief Модель достижения
    @param title Название достижения, максимальная длина - 150 символов
    @param description Описание достижения
    @param photo_album_url ссылка на фото-альбом
    @param link_to_media ссылка на СМИ
    """
    title = models.CharField(
        'название',
        max_length=150,
    )
    description = models.TextField(
        'описание',
    )
    photo_album_url = models.URLField(
        'ссылка на фото-альбом',
        blank=True,
    )
    link_to_media = models.URLField(
        'ссылка на СМИ',
        blank=True,
    )
    is_main = models.BooleanField(
        'главное достижение',
        default=False,
    )

    class Meta:
        verbose_name = 'достижение'
        verbose_name_plural = 'достижения'

    @staticmethod
    def get_all_objects_by_id():
        return Achievement.objects.order_by('-id')

    @staticmethod
    def get(id):
        return Achievement.objects.get(id=id)


class MainAchievement(models.Model):
    """!
    @brief Модель главного достижения (не отображается в админ панели)

    @param main_achievement Достижение, которое является главным
    """
    main_achievement = models.ForeignKey(
        'Achievement',
        on_delete=models.CASCADE,
    )

    @staticmethod
    def create(achievement):
        new_main_achievement = MainAchievement(
            main_achievement=achievement
        )
        new_main_achievement.save()

    @staticmethod
    def update(achievement):
        last_main_achievement = MainAchievement.objects.latest('id').main_achievement
        if achievement != last_main_achievement:
            last_main_achievement.is_main = False
            last_main_achievement.save()
        MainAchievement.create(achievement)


@receiver(post_save, sender=Achievement)
def update_main_achievement(sender, instance: Achievement, created, **kwargs):
    """!
    @brief Обработчик создания достижения.
    Предыдущее главное достижение делает обычным, если созданное/изменённое достижение стало главным.

    @param sender: источник сигнала
    @param instance: созданный объект
    @param created: признак того, что объект был создан (или изменён)
    @param kwargs: дополнительные параметры
    """
    if not instance.is_main:
        return
    if MainAchievement.objects.count() == 0:
        MainAchievement.create(instance)
    else:
        MainAchievement.update(instance)
