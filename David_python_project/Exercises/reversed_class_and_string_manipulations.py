def reversed_number(numbers):
    reversed_ = str(numbers)[::-1]
    return int(reversed_)


def reversed_list(list_):
    reversed_ = list_[::-1]
    return reversed_


def upper_cased_letter(words):
    return str(words).upper()


def lower_cased_letter(words):
    return str(words).lower()


def capitalize_first_letter(word):
    return str(word).capitalize()


def lower_cased_first_letter(word):
    return str(word[0]).lower() + str(word[1:]).upper()


if __name__ == '__main__':
    print(reversed_number(12345))
    print(reversed_list([1, 2, 3, 4, 5]))
    print(upper_cased_letter("david"))
    print(lower_cased_letter("DAVID"))
    print(capitalize_first_letter("david"))
    print(lower_cased_first_letter("DAVID"))

