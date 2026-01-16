# Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


# ------------------------------
# MY HOMEBREW SOLUTION - CRAP
def isPalendromeNumber(num):
    if num <0:
        print('False')
        return False
    numArray = []

    while num > 0:
        numArray.append(num % 10)
        num //= 10
  
    left = 0
    right = len(numArray) - 1
    while left < right:
 
        if numArray[left] != numArray[right]:
            print('False')
            return False
        left += 1
        right -= 1
    
    print('True')
    return True
    

# --------- PERFORMANT SOLUTION -------------

def isPalendromeNumberPerformant(num) -> bool:
    if num < 0:
        return False
    
    reversed_num = 0
    temp_num = num

    while temp_num != 0:
        last_digit = temp_num % 10
        
        reversed_num = reversed_num * 10 + last_digit
        print(reversed_num)
        temp_num //= 10
    
    return reversed_num == num



isPalendromeNumberPerformant(252)
    

    
    