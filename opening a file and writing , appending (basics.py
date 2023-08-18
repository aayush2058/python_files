# Reading a file

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
file.close()



# Writing into a file

'''
Below method overrides all of the content with new content in the file.
'''

file = open('data.txt', 'w')
content = 'Something written with file handling'
file.write(content)

file.close


'''
This helps prevent overriding the contents.
'''
file = open('data.txt', 'a')      # a is append mode, which appends content
file.write('\n' + content + '------- appending')        # \n is for new line
file.close()
