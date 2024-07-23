from django.db import models

from rs_back.core.models import ImageBaseModel


class News(ImageBaseModel):
    """
    Модель новости
    """
    title = models.CharField(
        'название',
        max_length=150
    )
    description = models.TextField(
        'описание',
    )
    new_url = models.URLField(
        'ссылка на новость',
    )

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    @staticmethod
    def get_all_objects_by_id():
        return News.objects.order_by('-id')
