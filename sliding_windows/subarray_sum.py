# Given an integer array nums and an integer k, 
# find the sum of the subarray with the largest sum whose length is k.

def largest_sum_subarray(intArray, k):
    rightPos = currSum = 0
# build the first subarray
    while rightPos < k:
        currSum += intArray[rightPos]
# this loop ends and rightPos is now == k - and then doesn't iterate anymore - i.e. == 3
        rightPos += 1
# set ans AFTER currSum for first window is calculated
    ans = currSum

    # rightPos is now at element k, which isn't in currSum yet
    for rightPos in range(rightPos, len(intArray)):
        # don't need leftPos pointer because fixed window
        currSum += intArray[rightPos] - intArray[rightPos - k]

        ans = max(ans, currSum)

    print(ans)
    return ans



largest_sum_subarray([3,7,2,9,4,1,6,5], 3)
