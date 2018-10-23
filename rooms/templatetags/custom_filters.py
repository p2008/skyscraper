from django.template import Template
from django import template

register = template.Library()


@register.filter
def if_yes_no(value):
    if value:
        return 'Yes'
    else:
        return 'No'

