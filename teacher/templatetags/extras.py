from django import template

register = template.Library()

@register.filter(name = 'get_val')
def get_val(dict, keys):
    return dict.get(keys)