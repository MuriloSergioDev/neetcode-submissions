class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if(len(s) % 2 != 0):
            return False

        for char in s:
            if(char == '('):
                stack.append(char)

            if(char == '['):
                stack.append(char)

            if(char == '{'):
                stack.append(char)

            if(len(stack) <= 0):
                return False

            if(char == ')'  and '(' != stack.pop()):
                return False

            if(char == ']' and '[' != stack.pop()):
                return False
            
            if(char == '}' and '{' != stack.pop()):
                return False
        
        if(len(stack) > 0):
            return False

        return True