if __name__ == '__main__':
    s = 'I want two things in life loving you and be loved by you'
    # print(s.upper())
    # print(s.lower())
    # print(s.capitalize())
    # print(s.title())
    # print(s.swapcase())
    # print(s.casefold())
    #
    # print(s.count("you"))
    # print(s.count("i"))
    # print(s.count('o'))
    # print(s.count('o', 10, 40))

    # print(s.find('you'))
    # print(s.index('you'))
    # # print(s.rfind('z'))
    # # print(s.rindex('you'))
    # # print(s.rindex('you', s.find("you") + 1 ))
    # # print(s.startswith("I want"))    # return true if the word("I want") starts the sentence and returns false if it
    # # # is not true
    # # print(s.endswith("you"))         # return true if the word(" you ") ends the sentence and returns false if it is
    # # # not true
    # print(s.isalnum())      # returns true if there is an alphanumeric word in the sentence
    # print(s.isalpha()) # todo note that this doesn't work with words that have spaces in them, use(replace(" ", "")  to use them
#
# import string
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.printable)
# print(string.punctuation)

# print(s.replace(" ", "$"))
# print(s.replace(" ", "$", 2))
#
# hello = "hello"
# print(hello.ljust(20, '*'))
# print(hello.rjust(20, '*'))
# print(hello.center(20, '*'))

# for i in range(1, 20, 2):
#     s = '*' * i
#     print(s.center(20))
#
# for i in range(1, 20, 2):
#     s = '*' * i
#     print(s.rjust(20))
#
#     for i in range(1, 20, 2):
#         s = '*' * i
#         print(s.ljust(20))


# num = '100010110'.replace('1', '2').replace('0', '1').replace('2', '0')
# print(num)
# print(num.translate(str.maketrans('01', '10')))

# import string
# word = input("Enter a word: ")
# key = int(input("Enter the key to code with: "))
# abc = string.ascii_lowercase
#
# inverse = abc[key:] + abc[:key]
#
# print(word.translate(str.maketrans(inverse, abc)))
#
# b = "my name is sinbi"
# # b = b[:5] + 'y' + b[6:]
#
# b = b[:1] + 'r ' + b[3:]
# h = "Hello nigeria"
# y = "I want to japa"
# value = h + y
# print(value)


course = 'Python for beginners'
print('python' in course)

