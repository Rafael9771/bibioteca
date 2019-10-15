from django import template

register = template.Library()

@register.filter
def to_and(value,val,replaced):
    return value.replace(val,replaced)