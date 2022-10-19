
test_input = "`l;`` 1o1 ??;l`"

def real_palindrome(string):
    string = string.lower()
    for character in string:
        if ord(character) not in range(97, 123) and character.isdigit() == False:
            string = string.replace(character, '')

    new_string = ''.join(string.split())
    return new_string == new_string[::-1]

print(real_palindrome(test_input))



