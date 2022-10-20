
test_input = [4,1,2,1,2]

def single_number(array):
    for element in array:
        if array.count(element) == 1:
            return element
    return -1


print(single_number(test_input))