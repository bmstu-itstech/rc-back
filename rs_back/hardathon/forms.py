from django import forms
from django.forms import FileInput

from rs_back.hardathon.models import Hardathon, Project


class HardathonForm(forms.ModelForm):
    """
    Форма для админ панели хардатонов
    Нужна для того, чтобы расширить зону загрузки файлов
    """
    class Meta:
        model = Hardathon
        fields = '__all__'
        widgets = {
            'photo': FileInput(
                attrs={
                    'style': 'border: 1px solid #353535; padding: 5em; border-radius: 4px',
                }
            ),
            'organizers_photo': FileInput(
                attrs={
                    'style': 'border: 1px solid #353535; padding: 5em; border-radius: 4px',
                }
            ),
        }


class ProjectForm(forms.ModelForm):
    """
    Форма для админ панели проектов
    Нужна для того, чтобы расширить зону загрузки файлов
    """
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'photo': FileInput(
                attrs={
                    'style': 'border: 1px solid #353535; padding: 5em; border-radius: 4px'
                }
            ),
        }
