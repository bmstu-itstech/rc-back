from django.contrib import admin

from rs_back.achievement.forms import AchievementForm
from rs_back.achievement.models import Achievement


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
