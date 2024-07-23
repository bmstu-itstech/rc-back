from django.contrib import admin
from django.db import OperationalError

from rs_back.achievement.forms import AchievementForm, AchievementOrderForm
from rs_back.achievement.models import Achievement, AchievementOrder


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


@admin.register(AchievementOrder)
class AchievementOrderAdmin(admin.ModelAdmin):
    """
    Админ панель для порядка достижения
    """
    list_display = (
        'order',
        'achievement',
    )
    list_display_links = ('order', 'achievement',)
    readonly_fields = ('order',)
    form = AchievementOrderForm
    search_fields = ('order', 'achievement',)
