
test_input = -123

def reverse_integer(number):

    is_negative = False

    if number < 0:
        is_negative = True
        number = abs(number)
    reversed_number = 0

    while number != 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    
    if is_negative:
        return -reversed_number

    return reversed_number

print(reverse_integer(test_input))
