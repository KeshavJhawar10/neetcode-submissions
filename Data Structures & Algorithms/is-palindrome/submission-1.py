class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1
        while start <= end:
            if s[start].isalnum() != True:
                start += 1
            elif s[end].isalnum() != True:
                end -= 1
            else:
                front_char = s[start].lower()
                end_char = s[end].lower()
                if front_char != end_char:
                    return False
                start +=1
                end -= 1
        return True