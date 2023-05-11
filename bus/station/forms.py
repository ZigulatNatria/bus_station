from captcha.fields import CaptchaField
from django import forms
from django.forms import ModelForm, CharField
from .models import RoutesCity, News, Vacancies, Timetable, Information
from tinymce.widgets import TinyMCE


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    telephone = forms.CharField(max_length=50, label='Телефон') #вписать именно на цифры
    # telephone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, label='Осебе')
    captcha = CaptchaField() #поле для капчи


class RoutesCityForm(ModelForm):

    content = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) # Виджет редактора

    class Meta:
        model = RoutesCity
        fields = [
            'number',
            'track',
            'content',
        ]

class NewsForm(ModelForm):

    text = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) # Виджет редактора

    class Meta:
        model = News
        fields = [
            'news_header',
            'image',
            'text',
            'file',
        ]


class VacanciesForm(ModelForm):

    info = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) # Виджет редактора

    class Meta:
        model = Vacancies
        fields = [
            'name',
            'vacancies_img',
            'info',
        ]


class TimetableForm(ModelForm):

    class Meta:
        model = Timetable
        fields = [
            'name',
            'image',
            'text',
            'file',
            'link',
        ]


class InformationForm(ModelForm):

    class Meta:
        model = Information
        fields = [
            'name',
            'text',
            'file',
        ]
