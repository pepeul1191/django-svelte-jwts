from django import template
from .settings import ENV

register = template.Library()

@register.simple_tag
def load_env():
    return ENV