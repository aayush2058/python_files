'''
Exception handling
'''

age = int(input('Enter your age : '))
try:
    assert age > 0      # checks if the number is positive
except AssertionError:          # something happened that developer thought would not happen
    print('age should be positive')     # if requirement doesn't meet
else:
    print('age is positive')    # if requirement meets
finally:
    print('This statement is closed')       # This is to be executed no matter the above result

'''
This can be done with few lines of code but the main concept here is to understand (Exception handling) in python

NO MATTER WHAT HAPPENS, OUR PROGRAM MUSTNOT CRASH WHEN CONSUMER USES IT. THEREFORE, EVERY POSSIBLE EXCEPTIONS SHOULD BE HANDELED BY THE DEVELOPER
'''
