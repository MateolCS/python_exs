
test_input = "The quick brown fox jumps over the lazy dog"

def pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in letters:
        if letter not in sentence.lower():
            return False
    return True

print(pangram(test_input))