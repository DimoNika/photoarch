from django import template


register = template.Library()





@register.simple_tag
def add(a, b):
    return a + b


@register.filter
def index_of_divisible_by(my_list: list, item, divisor):
    try:
        index = my_list.index(item)
        return index % divisor != 0
    except (ValueError, ZeroDivisionError):
        return False
    
# @register.simple_tag
# def multiply(a, b):
#     return a * b