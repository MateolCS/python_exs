

def happy_number(num):
    if num == 1:
        return True
    while num != 1:
        num = sum([int(i)**2 for i in str(num)])
        if num == 1:
            return True
        elif num == 4:
            return False
    
    return False

