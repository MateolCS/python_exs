
test_input =  'LVIII'

def roman_to_integer(roman_number):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_number = 0

    for i in range(len(roman_number)):
        if i > 0 and roman_numbers[roman_number[i]] > roman_numbers[roman_number[i - 1]]:
            integer_number += roman_numbers[roman_number[i]] - 2 * roman_numbers[roman_number[i - 1]]
        else:
            integer_number += roman_numbers[roman_number[i]]

    return integer_number

print(roman_to_integer(test_input))

