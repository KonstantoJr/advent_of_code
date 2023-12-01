"""Solution for Advent of Code Challenge Day 1 part 2"""
with open ("input.txt", "r", encoding='utf-8') as input_file:
    input_data = input_file.read().splitlines()

digits = []
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']

for line in input_data:
    found = False
    first = ""
    for letter in line:
        first += letter
        if letter.isdigit():
            first= letter
            break
        for number in numbers:
            if number in first:
                first = str(numbers.index(number))
                found = True
                break
        if found:
            break

    last = ""
    found = False
    for letter in line[::-1]:
        last += letter
        if letter.isdigit():
            last = letter
            break
        for number in numbers:
            if number in last[::-1]:
                last = str(numbers.index(number))
                found = True
                break
        if found:
            break


    # convert the digits to integers
    value = int(first + last)
    digits.append(value)


print(sum(digits))
