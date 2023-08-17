'''
Decorating a function with another function
'''


def clothes(func):      # This function can be used to decorate other functions
    def cloth_for(*args, **kwargs):     # This allows our function to have any number of arguments passedn in both formats i.e variable length and keyword length
        print(f'Here is {func(*args, **kwargs)} inside some clothes')
    return cloth_for

# Example 1
@clothes        # One of the way to use function on another function
def something_feeling_cold():       # This is go through clothes function to apply modifications on it without having to change contents on this function.
    return 'my dog'                # This will only apply the changes, we need to call function separately

something_feeling_cold()        # Calling above function to display

print() # to add a empty line

# Example 2
@clothes
def shivering(body_part):
    return body_part

shivering('hand')