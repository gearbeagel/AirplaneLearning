from django import template

register = template.Library()


@register.filter
def get_value(dictionary, key):
    if dictionary is None or key is None:
        return None
    return dictionary.get(key)

register.filter('get_value', get_value)
