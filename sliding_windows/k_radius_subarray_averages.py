# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements 
# in nums between the indices i - k and i + k (inclusive). If there are less than k elements 
# before or after the index i, then the k-radius average is -1.

# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]

# Input: nums = [100000], k = 0
# Output: [100000]

# Input: nums = [8], k = 100000
# Output: [-1]


def sub_array_averages(array, k):
    # if i < k, array[i] = -1, if i > len(array - k), array[i] = -1
    # average = total sum / total nums
    # iterate, add i to subarray until total nums = i[k] + k
    # calculate average on that subarray once full, move "subarray window"
    # for every iteration, if i < k array_to_return.append(-1),
    # running_total += array[i] until i[k] + k reached
    # array_to_return.append(running_total / i + k (number of elements)
    array_to_return = []
    running_total = 0
    rightPos = 0
    leftPos = 0
    for i in range(len(array)):
        # possibly put in conditional
        if i < k or i > len(array) - k:
            array_to_return.append(-1)
        running_total += array[i]
        while rightPos - leftPos + 1 == k + k + 1:
            array_to_return.append(running_total / k + k)
            running_total -= array[leftPos]
            leftPos -= 1
        rightPos += 1

    print(array_to_return)
# finish the rest of the array of negative 1s and look at average calc
sub_array_averages([7,4,3,9,1,8,5,2,6],3)
