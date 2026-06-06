class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_item=height[0]
        left_max=[height[0]]
        rt_max=[height[-1]]
        max_item_rt=height[-1]

        for i in range(1,len(height)):
            max_item=max(max_item,height[i-1])
            # print(i,max_item)
            left_max.append(max_item)

        # print('--------------')
        for i in range(len(height)-2,-1,-1):
            max_item_rt=max(max_item_rt,height[i+1])
            # print(i,max_item_rt)
            rt_max.append(max_item_rt)

        rt_max.reverse()
        # print(left_max)
        # print(rt_max)

        res=0
        for i in range(len(height)):
            temp=min(left_max[i],rt_max[i])-height[i]
            if temp>0:
                res+=temp

        return res