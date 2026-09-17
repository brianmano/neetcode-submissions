class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in closeToOpen: #seeing if the thing in s is closing
                if stack and stack[-1] == closeToOpen[c]: #if the stack at the top matches the open value
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) #append the opening
        
        if stack:
            return False
        else:
            return True