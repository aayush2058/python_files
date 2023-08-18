''' Reading a file

Please make a file named 'data.txt' inside the same directory and write some lines for below code to work.
'''

file = open('data.txt', 'r')
'''
contents = file.read(10)  # 10 is the number of bytes. In our case, it is displaying only the first 10 words in the file.
print(contents)
'''
line = file.readline() # This reads the first line of the file
print(line)

'''
We need to close a file after opening it because another program might not be able to open the same file in proper manner.
So,
'''
file.clos