test_input = [2,7,11,15]


def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum(test_input, 9))