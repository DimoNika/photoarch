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
    

@register.filter(name='split_into_four')
def split_into_four(value):

    def spin():
        x = -1
        while x < 4:
            x += 1
            if x == 4:
                x = -1
                continue
            yield x

    generator = spin()

    array = [[], [], [], []]

    for i in value:
        array[next(generator)].append(i)

    return array    
