from django.db import models

from rs_back.core.models import ImageBaseModel


class Director(ImageBaseModel):
    """
    Модель руководителя
    """
    fio = models.CharField(
        'ФИО',
        max_length=150,
    )
    email = models.EmailField(
        'email',
        max_length=150,
    )
    role = models.CharField(
        'должность',
        max_length=150,
    )

    class Meta:
        verbose_name = 'руководитель'
        verbose_name_plural = 'руководители'

    @staticmethod
    def get_all_objects_by_id():
        return Director.objects.order_by('-id')

    def __str__(self):
        return self.fio
