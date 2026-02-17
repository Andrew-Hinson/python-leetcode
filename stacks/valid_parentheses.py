# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

 #   Every open bracket is closed by the same type of close bracket.
 #   Open brackets are closed in the correct order.
 #   Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true

# Example 2:

# Input: s = "([{}])"

# Output: true


def is_valid(str):

    # iterate through str
    # as characters pushed to arr, check for coresponding closing type
    # return false if stuff dont match
    # if we are on index x
    # l can be used to check for match

    stack = []
    bracket_map = { ")" : "(", "]" : "[", "}" : "{" }

    for c in str:
        # if c is a CLOSING bracket
        if c in bracket_map:
            # when we see a closing bracket we check if the top of the stack has its match
            # and only if the stack is NOT empty
            if stack and stack[-1] == bracket_map[c]:
                stack.pop()
            # if the check is false its not a valid string
            else:
                return False
        # if its not a closing bracket it gets appended
        else:
            stack.append(c)
        
    # only return True if stack is empty because it could be something like "(((", all brackets must have a match
    return True if not stack else False


# "([{}])"
# "([]}"

is_valid("[()]")
