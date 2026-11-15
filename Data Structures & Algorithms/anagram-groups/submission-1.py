class Solution:
    def groupAnagrams(self, strs):
        dictionary={}
        for i in strs:
            key =''.join(sorted(i))
            if key in dictionary:
                dictionary[key].append(i)
            else:
                dictionary[key]=[i]
        return list(dictionary.values())