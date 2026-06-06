class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        res=[]
        if nums==[]:
            return 0  
        cur_item=nums[0]
        count=0
  
        for i in nums[1:]:
            if i == cur_item+1:
                count+=1
                cur_item=i
            elif i== cur_item:
                continue
            else:
                res.append(count)
                cur_item=i
                count=0

        if res == [] or count not in res:
            res.append(count)

        return max(res)+1