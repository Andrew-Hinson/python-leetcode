#given an array, create a new array that
#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]


def get_concat(nums):

    n = len(nums)
    ans = [0] * n * 2

    for i in range(len(nums)):
        
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    print(ans)
    return ans


get_concat([1,4,1,2])
