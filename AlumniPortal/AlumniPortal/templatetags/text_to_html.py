__author__ = 'ankur'

from django import template
register = template.Library()

@register.filter(name='text_to_html')
def text_to_html(text):
    return "<p>" + text.replace('\n', "</p><p>") + "</p>"