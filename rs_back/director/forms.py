from django import forms
from django.forms import EmailInput, FileInput, TextInput

from rs_back.director.models import Director


class DirectorForm(forms.ModelForm):
    """
    Форма для админ панели руководителей
    Нужна для того, чтобы расширить зону загрузки файлов
    """

    class Meta:
        model = Director
        fields = ('photo', 'fio', 'email', 'role')
        widgets = {
            'photo': FileInput(attrs={'style': 'border: 1px solid #353535;'
                                               'padding: 5em;'
                                               'border-radius: 4px'}),
            'fio': TextInput,
            'email': EmailInput,
            'role': TextInput,
        }
