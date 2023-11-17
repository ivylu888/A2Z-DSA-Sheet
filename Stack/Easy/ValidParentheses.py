"""
    Check for Balanced Parentheses
    Problem Statement: Check Balanced Parentheses. Given string str containing just the characters ‘(‘, ‘)’, ‘{‘, ‘}’, ‘[‘ and ‘]’, check if the input string is valid and return true if the string is balanced otherwise return false.
    
    Note: string str is valid if:
    
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:    
    Input: str = “( )[ { } ( ) ]”    
    Output: True
    
    Explanation: As every open bracket has its corresponding 
    close bracket. Match parentheses are in correct order 
    hence they are balanced.

    Example 2:    
    Input: str = “[ ( )”    
    Output: False
    
    Explanation: As '[' does not have ']' hence it is 
    not valid and will return ∏alse.
"""

class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen: #check dic[key] is close or not
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False #if stack is empty ->True
      

if __name__ == "__main__":
  valid_parentheses_instance = ValidParentheses()  # Create an instance of the class
  test_str = "(){}[]"
  print(valid_parentheses_instance.isValid(test_str))  # Call the method on the instance