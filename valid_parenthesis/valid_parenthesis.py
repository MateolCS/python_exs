

test_input = "(){}[]"

def valid_parenthesis( s ):
    cases = {
        '(': ')',
        '{': '}',
        '[': ']'}
    i = 0
    if len(s) % 2 != 0:
        return False

    while i < len(s):
        if cases[s[i]] == s[len(s) - 1 - i]:
            i += 1
            break
        else:
            return False
             
    return True

def test(s):
    open = [{'(': 0}, {'{': 0}, {'[': 0}]
    close = [{')': 0}, {'}': 0}, {']': 0}]

    for i in s:
        for j in open:
            if i in j:
                j[i] += 1
        for k in close:
            if i in k:
                k[i] += 1

    for i in range(len(open)):
        if list(open[i].values())[0] != list(close[i].values())[0]:
            return False
    return True

print(test(test_input))
    




