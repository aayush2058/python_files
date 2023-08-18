'''
Please make a file named 'data.txt' inside the same directory and write some lines for below code to work.

using (with), we donot need to close a file. It is handy isn't it?
'''

with open('data.txt', 'r') as file:
    contents = file.readlines()       # This returns a list of contents with a '\n' after each line.

print(contents)
print()     # adding blank line between two print statements.

for line in contents:
    print(line.strip())     # There is an extra line break due to '\n'. We can always use strip() method.
                            # lstrip() for left and rstrip() for right can be used as well.