from django.contrib import admin

from rs_back.news.forms import NewsForm
from rs_back.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Админ панель для новости
    """
    list_display = (
        'small_photo_tmb',
        'title',
        'new_url',
    )
    list_display_links = ('small_photo_tmb', 'title',)
    readonly_fields = ('photo_tmb',)
    form = NewsForm
    search_fields = ('title',)
