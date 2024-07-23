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
