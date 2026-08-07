from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {}
        left = right = 0
        
        while right < len(s2):
            s2_map[s2[right]] = 1 + s2_map.get(s2[right], 0) 
            if right - left + 1 == len(s1):
                
                if s1_map == s2_map:
                    return True
                s2_map[s2[left]] = s2_map.get(s2[left],0) - 1
                if s2_map[s2[left]] <= 0:
                    del s2_map[s2[left]]
                left+=1
            right+=1    
        return False