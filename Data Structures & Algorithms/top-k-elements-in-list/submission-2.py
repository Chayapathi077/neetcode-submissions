class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        l=[]
        one=[]
        for i in nums:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
            
        l = sorted(dictionary, key=dictionary.get, reverse=True)
        return l[:k]