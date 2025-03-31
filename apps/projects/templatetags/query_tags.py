from django import template

register = template.Library()

@register.simple_tag(takes_context=True)  # Version optimisée
def query_transform(context, **kwargs):
    """
    Tag pour modifier les paramètres d'URL sans perdre les existants
    Usage: {% query_transform page=2 search='django' %}
    """
    request = context['request']
    updated = request.GET.copy()
    for key, value in kwargs.items():
        if value:
            updated[key] = value
        else:
            updated.pop(key, None)
    return updated.urlencode()