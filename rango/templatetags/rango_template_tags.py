from django import template
from rango.models import Category

register=template.Library()

@register.inclusion_tag('rango/cats.html')
def get_cat_list(thing=None):
    return {'things': Category.objects.all(),'act_thing':cat}


