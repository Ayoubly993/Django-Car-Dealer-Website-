from django import template
from math import floor
register = template.Library()

@register.filter(name='division')
def division(value):
    try:
        return floor(int(value) / 48) # 4 years
    except (ValueError, ZeroDivisionError):
        return None