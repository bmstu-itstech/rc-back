from django.core.validators import MinValueValidator
from django.db import models

from rs_back.core.models import ImageBaseModel


class Achievement(ImageBaseModel):
    """
    Модель достижения
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

    class Meta:
        verbose_name = 'достижение'
        verbose_name_plural = 'достижения'

    @staticmethod
    def get_all_objects_by_id():
        return Achievement.objects.order_by('-id')


class AchievementOrder(models.Model):
    """
    Модель порядка достижений
    """
    achievement = models.OneToOneField(
        'Achievement',
        on_delete=models.CASCADE,
        null=True,
        default=None,
        blank=True,
        verbose_name='достижение'
    )
    order = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='порядок',
    )

    class Meta:
        verbose_name = 'порядок достижений'
        verbose_name_plural = 'порядок достижений'

    @staticmethod
    def generate(count=4):
        if AchievementOrder.objects.count() == 0:
            for i in range(count):
                new_object = AchievementOrder(
                    order=i + 1,
                    achievement=None
                )
                new_object.save()

    @staticmethod
    def get_all_objects_by_order():
        return AchievementOrder.objects.order_by('order')
