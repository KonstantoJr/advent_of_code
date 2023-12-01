"""Solution for Advent of Code Challenge Day 1 part 1"""
with open ("input.txt", "r", encoding='utf-8') as input_file:
    input_data = input_file.read().splitlines()

digits = []

for line in input_data:
    # find the first digit in the string and then the last
    # the string is a list of characters
    for letter in line:
        if letter.isdigit():
            first= letter
            break
    for letter in line[::-1]:
        if letter.isdigit():
            last = letter
            break

    # convert the digits to integers
    value = int(first + last)
    digits.append(value)


print(sum(digits))
