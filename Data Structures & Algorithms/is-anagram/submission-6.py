class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        S = {}
        T = {}

        for i in range(len(s)):
            if s[i] in S:
                S[s[i]] += 1
            else:
                S[s[i]] = 1

            if t[i] in T:
                T[t[i]]+=1
            else:
                T[t[i]]=1

        return S == T