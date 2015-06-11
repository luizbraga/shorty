from django import template

register = template.Library()

@register.simple_tag
def short_it(link):
    shortener = Shortener('GoogleShortener')
    return format(shortener.short(self.url))