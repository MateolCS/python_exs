

def majorityElement(nums):
        for number in nums: 
            if nums.count(number) > len(nums)/2:
                return number
        return -1