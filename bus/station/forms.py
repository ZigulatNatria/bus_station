from captcha.fields import CaptchaField
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    telephone = forms.CharField(max_length=50, label='Телефон') #вписать именно на цифры
    # telephone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, label='Осебе')
    captcha = CaptchaField() #поле для капчи