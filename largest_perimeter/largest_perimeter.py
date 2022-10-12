
test_input = [1, 2, 1]

def largest_perimeter(nums):
    nums.sort(reverse=True)
    print(nums)
    max_perimeter = 0
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            if nums[i] + nums[i+1] + nums[i+2] > max_perimeter:
                max_perimeter = nums[i] + nums[i+1] + nums[i+2] 
    return max_perimeter

print(largest_perimeter(test_input))
        