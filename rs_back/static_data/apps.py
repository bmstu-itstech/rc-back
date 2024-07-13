from django.apps import AppConfig


class StaticDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rs_back.static_data'
    verbose_name = 'Статические данные'
