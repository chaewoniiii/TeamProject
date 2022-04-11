from dataclasses import replace
from django import template
import re
register = template.Library()

@register.filter('idreplace')
def idreplace(id):
    # id -> admin2, user2 ...
    id_s = str(id)[2:]
    id_star = '*' * len(id_s)
    return str(id)[:2] + id_star
