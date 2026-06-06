class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        freq={}
        for i in nums:
            freq[i]=False
        longest_length=0
        cur_length=0
        res_length=0

        for i in nums:
            cur_length=i
            longest_length=0
            if freq[cur_length]==False: 
                freq[cur_length]=True
                longest_length+=1
            num_next=cur_length+1
            flag=True
            while flag: 
                if num_next in nums:
                    freq[num_next]=True
                    longest_length+=1
                    num_next+=1
                else:
                    flag=False
            flag=True
            num_prev=cur_length-1
            while flag: 
                if num_next in nums:
                    freq[num_next]=True
                    longest_length+=1
                    num_prev-=1
                else:
                    flag=False
            res_length=max(longest_length,res_length)
        return res_length