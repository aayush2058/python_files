'''
 Variable length positional argument
'''

# Simple function to add two arguments
def sum(a, b):
    sum = a + b
    return sum

print(sum(10, 5))

'''
Suppose we want to make this function work on any number of given arguments without any error.
'''
def sum(*number):     # '*' takes any number of given arguments/ 'number' is a parameter name
    sum = 0
    for i in number:
        sum = i + sum
    return sum

print(sum(1,2,3,4,5,6,7,8,9))