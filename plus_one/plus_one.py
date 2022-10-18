
test_input = [1, 2, 3]

def plus_one(array):
    integer = int(''.join(map(str, array))) + 1
    return [int(digit) for digit in str(integer)]

print(plus_one(test_input))