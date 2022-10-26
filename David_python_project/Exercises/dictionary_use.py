# if __name__ == '__main__':
#     paragon = {
#         "name_one": "John Doe",
#         "name_two": "Peter Dury",
#         "name_three": "Jim Berglin",
#         "name_four": "Lee min hu",
#         "name_five": "Kim jan di",
#         "name_six": "Kim na na"
#     }
#     print(paragon)
#
#     # todo To print a particular output out of the listed dictionary names
#     print(paragon["name_four"])
#
#     # todo To change a particular name out of the listed dictionaries
#     print(paragon["name_four"])
#     paragon["name_four"] = "Oladele"
#     print(paragon.values())
#
#     # todo To add a new value to the dictionary list
#     paragon["name_seven"] = "Oppa"
#     print(paragon)
#
#     # todo TO get a value from the dictionary lists
#     val = paragon.get("name_one")
#     print(val)
#
#     # todo To separate each keys and values by parenthesis
#     print(paragon.items())
#
#     # todo To show only the last item from the dictionary lists
#     print(paragon.popitem())


fist_dict = {
    "key_1": "I love python",
    "key_2": {
        "name": "paragon",
        "age": "4 months",
        "loan amount": "4 million",
        "size": 39,
        "weight": 9.9
    },
    "key_3": 500,
    "key_4": [50, 20, 45, "love python",["baba", "dada",["good", "bad"]]],
    "key_5": "fantastic"
}

print(fist_dict["key_2"]["size"])

print(fist_dict["key_4"][4][2][0])

# todo           OR

# print(fist_dict.get("key_2").get("size"))
