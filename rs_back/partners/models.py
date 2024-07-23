from django.db import models

from rs_back.core.models import ImageBaseModel


class Partner(ImageBaseModel):
    """
    Модель партнёра
    """
    title = models.CharField(
        'название',
        max_length=150,
        help_text='Максимум 150 символов',
    )
    link = models.URLField(
        'ссылка на сайт',
        blank=True,
    )

    class Meta:
        verbose_name = 'партнёр'
        verbose_name_plural = 'партнёры'

    @staticmethod
    def get_all_objects_by_id():
        return Partner.objects.order_by('-id')
