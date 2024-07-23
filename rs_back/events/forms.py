from django import forms
from django.forms import FileInput

from rs_back.events.models import ClassicEvent


class ClassicEventForm(forms.ModelForm):
    """
    Форма для админ панели событий
    Нужна для того, чтобы расширить зону загрузки файлов
    """
    class Meta:
        model = ClassicEvent
        fields = '__all__'
        widgets = {
            'photo': FileInput(
                attrs={
                    'style': 'border: 1px solid #353535; padding: 5em; border-radius: 4px',
                }
            ),
        }
