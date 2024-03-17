from django import template

register = template.Library()


@register.filter
def get_value(dictionary, key):
    return str(dictionary.get(key))


register.filter('get_value', get_value)
