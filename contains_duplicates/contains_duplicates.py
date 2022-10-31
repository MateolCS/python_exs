
test_input = [1, 2, 3, 1]

def contains_duplicates(nums):
    if len(nums) == len(set(nums)):
        return False
    return True

print(contains_duplicates(test_input))