from django.contrib import admin
from django.db import OperationalError

from rs_back.achievement.forms import AchievementForm, AchievementOrderForm
from rs_back.achievement.models import Achievement, AchievementOrder


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """!
    @brief Админ панель для достижения
    @param list_display Поля модели, отображаемые на сайте:
                        маленькое изображение, название, ссылка на СМИ
    @param list_display_links Поля, являющиеся ссылками
                              на страницу редактирования:
                              маленькое изображение, название
    @param readonly_fields Readonly поля: изображение
    @param form Форма для редактирования/создания
    @param search_fields Поля поиска
    """
    list_display = (
        'small_photo_tmb',
        'title',
        'link_to_media',
    )
    list_display_links = ('small_photo_tmb', 'title',)
    readonly_fields = ('photo_tmb',)
    form = AchievementForm
    search_fields = ('title',)


@admin.register(AchievementOrder)
class AchievementOrderAdmin(admin.ModelAdmin):
    """!
    @brief Админ панель для порядка достижения
    @param list_display Поля модели, отображаемые на сайте
    @param list_display_links Поля, являющиеся ссылками на страницу редактирования
    @param readonly_fields Readonly поля
    @param form Форма для редактирования/создания
    @param search_fields Поля поиска
    """
    list_display = (
        'order',
        'achievement',
    )
    list_display_links = ('order', 'achievement',)
    readonly_fields = ('order',)
    form = AchievementOrderForm
    search_fields = ('order', 'achievement',)
