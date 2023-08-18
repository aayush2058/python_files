# Palindrome checker

word = 'madam'

def palindrome_checker(word):
    if word == word[::-1]: # -->reverses the word
        print("Palindrome")
    else:
        print("Not palindrome")

    #----------OR------------

    # for i in range(len(word)):
    #     if word[i] == word[(len(word) - i - 1)]:
    #         palindrome_flag = True
    #     else:
    #         palindrome_flag = False
    #
    # if palindrome_flag:
    #     print('Palindrome')
    # else:
    #     print('Not Palindrome')

palindrome_checker('racecar')