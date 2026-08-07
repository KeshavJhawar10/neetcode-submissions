class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comps = {"}" : "{", ")" : "(", "]" : "["}
        for c in s:
            if c in comps:
                if stack and stack[-1] in comps[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False