'''
Decorating a function with another function
'''

# Suppose we have total price of the customer and want to apply seasonal discounts (winter and summer)

# decorators are always created at first

def summer_discount_decorator(function):
    def wrapper(price):
        total = price * 50 / 100
        return total
    return wrapper

def winter_discount_decorator(function):
    def wrapper(price):
        total = price * 25 / 100
        return total
    return wrapper




def total(price):
    return price

print(f'Your total is ${total(100)}')


@summer_discount_decorator
def total(price):
    return price

print(f'Your total after summer discount is ${total(100)}')


@winter_discount_decorator
def total(price):
    return price
print(f'Your total after winter discount is ${total(100)}')
