import datetime
from django import template
# from menu.models import MenuName

register = template.Library()

@register.simple_tag
def my_tag_date():
    return datetime.datetime.now().strftime('%Y')
