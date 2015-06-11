from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def short_it(context, link):
    request = context['request']
    http_host = request.META['HTTP_HOST']
    scheme = request.META['wsgi.url_scheme']
    return '%s://%s/%s' % (scheme, http_host, link.shortIt())