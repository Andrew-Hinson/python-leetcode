# You are given a binary string s (a string containing only "0" and "1").
# You may choose up to one "0" and flip it to a "1". 
# What is the length of the longest substring achievable that contains only "1"?
# For example, given s = "1101100111", the answer is 5.
# If you perform the flip at index 2, the string becomes 1111100111.

# every iteration, I add 1 to curr, if i reach 2 zeros, i subtract from current.
def flipZero(string):
    positionLeft = positionRight = curr = ans = 0

    for positionRight in range(len(string)):
        if string[positionRight] == '0':
            curr += 1
        while curr > 1:
            if string[positionLeft] == '0':
                curr -= 1
            positionLeft += 1
            
        ans = max(ans, positionRight - positionLeft + 1)
    print(ans)
    return ans
flipZero('1101100111')