class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res_list=[]
        for i in range(len(nums)-2):
            temp=[]
            temp.append(nums[i])
            lt_index=i+1
            rt_index=len(nums)-1
            while lt_index<rt_index:
                # print(lt_index,rt_index,i)
                # print(nums[lt_index],nums[rt_index],nums[i])
                # print('-------------------')
                if nums[lt_index]+nums[rt_index]+nums[i]==0:
                    temp.append(nums[lt_index])
                    temp.append(nums[rt_index])
                    if len(temp)==3:
                        if temp not in res_list:
                            res_list.append(temp)
                    # print(temp,res_list)
                    temp=[]
                    temp.append(nums[i])
                    lt_index+=1
                    rt_index-=1
                elif nums[lt_index]+nums[rt_index]+nums[i]>0:
                    rt_index-=1
                else:
                    lt_index+=1
            if len(temp)==3:
                if temp not in res_list:
                    res_list.append(temp)
        return res_list