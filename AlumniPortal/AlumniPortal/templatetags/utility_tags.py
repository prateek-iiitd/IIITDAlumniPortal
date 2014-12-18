__author__ = 'ankur'

from django import template

register = template.Library()


@register.assignment_tag(takes_context=False, name='get_all_degree')
# @register.filter(name='get_all_degree')
def get_all_degree():
    return ['btech', 'mtech', 'dual', 'phd']

#
# {#    {% load utility_tags %}#}
# {#    {% get_all_degree as pages %}#}
# {#    {% for page in pages %}#}
# {#         {{ page }}#}
# {#    {% endfor %}#}
