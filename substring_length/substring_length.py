
def contains(character, array):
    for i in range(len(array)):
        if character == array[i]:
            return True
    return False

test_input = "aab"


def substring_length(s):
    substr_length = 0
    chars = []
    possible_results = []
    i = 0
    while i in range(len(s)):
        if not contains(s[i], chars):
            substr_length = substr_length +1
            chars.append(s[i])
        else:
            possible_results.append(substr_length)
            chars = []
            substr_length = 0
            i -= 1
        i += 1
    possible_results.append(substr_length)

    return max(possible_results)
        
                

print(substring_length(test_input))