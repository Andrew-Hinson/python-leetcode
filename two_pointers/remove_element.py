# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.
# Input: nums = [1,1,2,3,4], val = 1

# Output: [2,3,4] (return 3)

# Input: nums = [0,1,2,2,3,0,4,2], val = 2

# Output: [0,1,3,0,4] (return 5)

# this problem demonstrates modifying an array in place using a 2 pointer solution, k and i being the pointers
# k increments when the val we dont want is NOT encountered. So it starts at 0 in this first example,
# the first 2 "1s" are encountered, k stays 0. Finally, 2 is encountered at index 2.
# k's 0 pos is then overwritten with the val at index 2 (2), and then incrimented. 
# the final array will have "garbage" values, but this problem does not ask us to resize the array,
# only return the count of all values that do not contain "val"
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(k) 
    return k




remove_element([1,1,2,3,4], 1)
