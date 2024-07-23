from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class ImageBaseModel(models.Model):
    """
    Базовая модель с изображением. Класс является абстрактным
    """
    photo = models.ImageField(
        'изображение к мероприятию',
        upload_to='photos/%Y/%m/%d',
        blank=True,
    )

    class Meta:
        abstract = True

    @property
    def get_photo(self):
        """
        Метод получения изображения
        """
        return get_thumbnail(self.photo, '300x300', crop='center', quality=51)

    def photo_tmb(self):
        """
        Метод получения тега изображения со ссылкой
        Если изображения нет, то возвращает строку *Нет изображения*.
        Если изображение есть, то возвращает тег *<img src="...">*
        """
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_photo.url}"',
            )
        return 'Нет изображения'

    photo_tmb.short_description = 'главное изображение'
    photo_tmb.allow_tags = True

    @property
    def get_small_photo(self):
        """
        Метод получения изображения маленького размера
        """
        return get_thumbnail(self.photo, '50x50', crop='center', quality=51)

    def small_photo_tmb(self):
        """
        Метод получения тега маленького изображения со ссылкой
        Если изображения нет, то возвращает строку *Нет изображения*.
        Если изображение есть, то возвращает тег *<img src="...">*
        """
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_small_photo.url}" ',
            )
        return 'Нет изображения'

    small_photo_tmb.short_description = 'главное изображение'
    small_photo_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        """
        Метод удаления изображения. Метод вызывается при удалении объекта из базы данных
        """
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title


class EventBaseModel(ImageBaseModel):
    """
    Базовая модель мероприятия
    Класс наследуется от ImageBaseModel и является абстрактным
    """
    title = models.CharField(
        'название',
        max_length=150,
        help_text='Максимум 150 символов',
    )
    description = models.TextField(
        'описание',
    )
    photo_album_url = models.URLField(
        'ссылка на фото-альбом',
        blank=True,
    )
    documents_url = models.URLField(
        'ссылка на документы',
        blank=True,
    )
    location = models.URLField(
        'место проведения',
    )
    event_date = models.DateField(
        'дата проведения',
    )
    social_media_mention = models.URLField(
        'упоминание в сми',
        blank=True,
    )

    class Meta:
        abstract = True
