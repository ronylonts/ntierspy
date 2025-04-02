from django import template
from django.http import QueryDict

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    """
    Modifie les paramètres GET existants dans l'URL
    Exemple d'utilisation : 
    <a href="?{% query_transform page=2 %}">Page 2</a>
    <a href="?{% query_transform page=2 search='django' %}">Page 2 avec recherche</a>
    """
    request = context.get('request')
    if not request:
        return ''
    
    params = request.GET.copy()
    
    for k, v in kwargs.items():
        if v is not None:
            params[k] = str(v)
        else:
            params.pop(k, None)
    
    return params.urlencode()

@register.filter
def get_item(dictionary, key):
    """Récupère un élément d'un dictionnaire par sa clé"""
    return dictionary.get(key)

@register.simple_tag
def active_nav(request, pattern):
    """Vérifie si le lien de navigation est actif"""
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''