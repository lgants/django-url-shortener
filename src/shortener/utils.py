import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # gives back random string
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # retrun new_code

    # for_ is shorthand where variable (i.e. _, i, etc.) is not being used but still want to run an iteration
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    
    # use class with a 'K' to be explicit that this inherited class
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
