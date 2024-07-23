from django.db import models

from rs_back.core.models import EventBaseModel
from rs_back.events.validators import ValidateFullName, ValidateGroup
from rs_back.partners.models import Partner


class ClassicEvent(EventBaseModel):
    """
    Модель классического мероприятия
    """
    registration_link = models.URLField(
        'ссылка на регистрацию',
    )
    partners = models.ManyToManyField(
        Partner,
        verbose_name='партнёры классического мероприятия',
        blank=True,
    )

    class Meta:
        verbose_name = 'классическое мероприятие'
        verbose_name_plural = 'классические мероприятия'

    @staticmethod
    def get_all_objects_by_id():
        return ClassicEvent.objects.order_by('-id')


class Questionnaire(models.Model):
    """
    Модель анкеты
    """
    searcher_fio = models.CharField(
        'фио участника',
        max_length=150,
        validators=[ValidateFullName()],
    )
    searcher_bmstu_group = models.CharField(
        'учебная группа',
        max_length=15,
        validators=[ValidateGroup()],
    )
    participants_count = models.IntegerField(
        'количество людей в команде',
    )
    required_competencies = models.TextField(
        'необходимые компетенции',
    )
    searcher_VK = models.URLField(
        'ссылка на ВКонтакте соискателя',
    )
    additional = models.TextField(
        'дополнительная информация',
        blank=True,
    )
    classic_event = models.ForeignKey(
        'ClassicEvent',
        verbose_name='классическое мероприятие',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'анкета'
        verbose_name_plural = 'анкеты'
        ordering = ['-id']

    @staticmethod
    def get_all_objects_by_id():
        return Questionnaire.objects.order_by('-id')

    def __str__(self):
        return self.searcher_fio
