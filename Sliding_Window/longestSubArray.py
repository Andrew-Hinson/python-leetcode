#  Given an array of positive integers nums and an integer k, 
# find the length of the longest subarray whose sum is less than or equal to k

def subArrayFinder(array, k):
    positionLeft, positionRight, curr, ans = 0

    for positionRight in range(len(array)):
        curr += array[positionRight]
        while curr > k:
            curr -= array[positionLeft]
            positionLeft += 1
    
        ans = max(ans, positionRight - positionLeft + 1)
    print(ans)
    return ans




subArrayFinder([1,2,3,4,5], 5)