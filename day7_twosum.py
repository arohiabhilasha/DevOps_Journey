# Problem: Given an array of integers [2, 7, 11, 15] and a target (9).
# Find two numbers that add up to the target.
# Return their indices (positions).
# Answer should be [0, 1] because 2 + 7 = 9.


#def two_sums(nums: list[int], target: int) -> list[int]:
#    for i in range(len(nums)):
#        for j in range(i + 1, len(nums)):
#            if nums[i] + nums[j] == target:
#                return [i, j]



#Approach 2, using hash map

def two_sum(nums: list[int], target: int) -> list[int]:
    num_list = {}
    for i in range(len(nums)):
        if target - nums[i] in num_list:
            return [num_list[target - nums[i]], i]
        num_list[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))