from django.contrib import admin

from rs_back.director.forms import DirectorForm
from rs_back.director.models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    """
    Админ панель для руководителя
    """
    list_display = (
        'small_photo_tmb',
        'fio',
        'email',
        'role',
    )
    list_display_links = ('small_photo_tmb', 'fio',)
    readonly_fields = ('photo_tmb',)
    form = DirectorForm
    search_fields = ('fio', 'email', 'role')
