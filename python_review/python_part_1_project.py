import random

value = random.randint(0, 10)


def odd_or_even(value):
    if value % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")


odd_or_even(value)


def sum_of_sequence():
    num = int(input("Enter a number: "))
    sequence = range(num + 1)
    sum_of_sequence = sum(sequence)
    return sum_of_sequence


result = sum_of_sequence()
print("The sum of the sequence is:", result)


def count_chars(text):
    digits = 0
    letters = 0
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1

    return {'digits': digits, 'letters': letters}


text = input("Enter a text: ")
result = count_chars(text)
print("Number of digits:", result['digits'])
print("Number of letters:", result['letters'])
print("Result dictionary:", result)
