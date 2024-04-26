from django import template

register = template.Library()

@register.filter(name='add_classes')
def add_classes(field, css_classes):
    return field.as_widget(attrs={'class': css_classes})