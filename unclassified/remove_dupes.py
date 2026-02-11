# You are given an integer array nums sorted in non-decreasing order.
# Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, 
# such that the first k elements of nums contain the unique elements.
# Input: nums = [1,1,2,3,4]
# Output: [1,2,3,4]
# k = 4

# what makes this problem tricky is modifying array IN PLACE instead of my first pass below

# def remove_dupes(list_of_nums):
#     unique_nums = []
#     for num in list_of_nums:
#         if num not in unique_nums:
#             unique_nums.append(num)
#     print(unique_nums)
#     return (unique_nums)

# this is kind of cheating, its not modifying the array in place it's just swapping it out
# - create unique_nums array - point num array at unique array - doesn't solve problem

# this method just checks if the next item is equal to the current item and removes the current item
# keeping the array in place.
# def remove_dupes(nums):
#
#
#     for i in range(len(nums)):
#         print("starting loop")
#         if i == len(nums) - 1:
#             print(f"at last element- {i}")
#             return nums
#         num = nums[i]
#         next_num = nums[i + 1]
#         if num == next_num:
#             nums.remove(num)
#
#
#     print(nums)
#     return nums

# this is a fundamental misunderstanding by me on what remove() does. will update. this is NOT correct
def remove_dupes(nums):

    for num in range(len(nums)):
        if nums[num] == nums[-1]:
            # not sure if they want the number of unique vals returned or the array returned
            print(nums)
            return nums
        if nums[num] == nums[num + 1]:
            nums.remove(nums[num])










remove_dupes([2,10,10,30,30,30])
