from django import forms
from django.forms import FileInput, Textarea, TextInput, URLInput

from rs_back.news.models import News


class NewsForm(forms.ModelForm):
    """
    Форма для админ панели новостей
    Нужна для того, чтобы расширить зону загрузки файлов
    """

    class Meta:
        model = News
        fields = ('photo', 'title', 'description', 'new_url')
        widgets = {
            'photo': FileInput(attrs={'style': 'border: 1px solid #353535;'
                                               'padding: 5em;'
                                               'border-radius: 4px'}),
            'title': TextInput,
            'description': Textarea,
            'new_url': URLInput,
        }
