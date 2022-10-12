
test_input = [1, 2, 1]

def largest_perimeter(nums):
    nums.sort(reverse=True)
    print(nums)
    if nums[0] >= (nums[1] + nums[2]):
            return 0
    return sum(nums)

print(largest_perimeter(test_input))
        