
from multiprocessing.reduction import duplicate


test_input = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
