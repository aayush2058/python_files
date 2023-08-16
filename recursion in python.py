# Factorial using Recursion
# Recursion means to reoccur multiple times

# factorial of 5 (5!) = 5*4*3*2*1

def factorial(number):
    if number == 1:     #because least possible number is one and it should not get stuck in loop
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))