import random


def split_str(s):
    return [ch for ch in s]


# https://samliew.com/nric-generator
# This will generate a valid NRICFIN with first char and age (age can be any with default -1)
def generate(first='S', age=-1):
    if first != 'S' and first != 'T' and first != 'F' and first != 'G':
        return

    # < option
    # value = "-1" > Any < / option >
    # < option
    # value = "1" > 2010 - 2019 < / option >
    # < option
    # value = "0" > 2000 - 2009 < / option >
    # < option
    # value = "9" > 1990 - 1999 < / option >
    # < option
    # value = "8" > 1980 - 1989 < / option >
    # < option
    # value = "7" > 1970 - 1979 < / option >

    if not (age >= -1 and age <= 9):
        age = -1

    chars = split_str(str(random.randint(0, 9999999)).zfill(7))

    if age != -1: chars[0] = age
    output = first + ''.join(chars)

    chars[0] = str(int(chars[0]) * 2)
    chars[1] = str(int(chars[1]) * 7)
    chars[2] = str(int(chars[2]) * 6)
    chars[3] = str(int(chars[3]) * 5)
    chars[4] = str(int(chars[4]) * 4)
    chars[5] = str(int(chars[5]) * 3)
    chars[6] = str(int(chars[6]) * 2)

    sum = 0
    for i in range(7):
        sum += int(chars[i])

    offset = 4 if (first == "T" or first == "G") else 0
    temp = (offset + sum) % 11
    st = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    fg = ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]

    if first == "S" or first == "T":
        alpha = st[temp]
    elif first == "F" or first == "G":
        alpha = fg[temp]
    else:
        alpha = "?"
    return output + alpha

