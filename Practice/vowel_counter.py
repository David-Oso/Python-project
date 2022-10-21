open_file = open("vowel.txt", "r")

find_word = ''
for word_line in open_file:
    for char in word_line:
        if char in ['a', 'e', 'i', 'o', 'u']:
            find_word += char

    if find_word == 'aeiou':
        print(word_line, end='')

    find_word = ''
