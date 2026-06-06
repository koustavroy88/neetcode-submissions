class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lf_arr=[1]*len(nums)
        rt_arr=[1]*len(nums)

        for i in range(1,len(nums)):
            lf_arr[i]=lf_arr[i-1]*nums[i-1]

        i=len(nums)-2
        while i>=0:
            rt_arr[i]=rt_arr[i+1]*nums[i+1]
            i-=1

        res=[]
        for i in range(len(nums)):
            res.append(lf_arr[i]*rt_arr[i])
        
        return res