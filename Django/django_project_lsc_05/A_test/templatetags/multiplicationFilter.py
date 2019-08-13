from django import template

register = template.Library()

@register.filter
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


