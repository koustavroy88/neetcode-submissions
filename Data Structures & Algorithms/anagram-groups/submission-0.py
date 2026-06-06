class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        res=[]
        for i in strs:
            if ''.join(sorted(i)) in freq:
                freq[''.join(sorted(i))].append(i)
            else:
                freq[''.join(sorted(i))]=[i]

        for i in freq:
            res.append(freq[i])
        return res