class Solution(object):
    def isValid(self,s):
        stack = [] #stores opening brackets
        for b in s:
            if b in '([{':
                stack.append(b)

            else:
                if not stack or \
                (b == ')'and stack[-1] != "(") or \
                (b == "}" and stack[-1] != "{") or \
                (b == ']' and stack[-1] != '['):
                    return False

                stack.pop()


        return not stack
