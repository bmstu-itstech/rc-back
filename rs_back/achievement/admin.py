from django.contrib import admin

from rs_back.achievement.forms import AchievementForm
from rs_back.achievement.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """
    Админ панель для достижения
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
