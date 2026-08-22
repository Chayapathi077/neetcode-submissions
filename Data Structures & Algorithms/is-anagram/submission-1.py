class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict(Counter(s))
        d2 = dict(Counter(t))
        if d1 == d2:
            return True
        else:
            return False

            
        