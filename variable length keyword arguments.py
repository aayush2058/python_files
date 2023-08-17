'''
Variable length keyword arguments
'''

def products(**args):
    for key, value in args.items():
        print(f'{key}  :  {value}')

products(name = 'Aayush', age = 22)
products(name = 'Aayush', age = 22, address = 'Vyas, Nepal')

'''
This function can take (any number of keyword arguments) and prints the result in the form of a key : value pair
'''