from django import template
from pyshorteners.shorteners  import Shortener

register = template.Library()

@register.simple_tag
def short_it(link):
    shortener = Shortener('TinyurlShortener')
    return shortener.short(link.url)