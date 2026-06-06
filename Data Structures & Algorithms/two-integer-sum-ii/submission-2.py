class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lt_index=0
        rt_index=len(numbers)-1

        while lt_index!=rt_index:

            if numbers[lt_index]+numbers[rt_index]==target:
                return [lt_index+1,rt_index+1]
            elif numbers[lt_index]+numbers[rt_index] > target:
                rt_index-=1
            else:
                lt_index+=1
                