# determine if a string is a palendrome (can be read backwards and forwards and is the same word)

def isPalendrome(s):
    left = 0
    right = len(s) - 1
   
    while left < right:
        if s[left] != s[right]:
            print("False")
            return False
        left += 1
        right -= 1

    print("True")
    return True