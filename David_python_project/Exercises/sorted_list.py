# my_list = list('xyzabc')
# print(my_list)
#
# my_list.sort()
# print()
# print(my_list)
#
# print()
# num = list('325435654354')
# print(num)
#
# print()
# num.sort()
# print(num)

def list_element(word, number):
    word_list = sorted(word)
    number_list = sorted(number)
    number_list2 = []

    for element in number_list:
        number_list2.append(int(element))

    print(word_list)
    print(number_list2)


if __name__ == '__main__':
    user_input = input("Enter a word: ")
    user_input2 = input("Enter a number: ")
    list_element(user_input, user_input2)