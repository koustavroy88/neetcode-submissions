class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt_index,rt_index,lt_height,rt_height=0,len(heights)-1,heights[0],heights[-1]
        area=(len(heights)-1)*min(lt_height,rt_height)
        while lt_index<rt_index:
            # print(lt_index,rt_index,lt_height,rt_height)
            if lt_height<rt_height:
                lt_index+=1
                lt_height=heights[lt_index]
            else:
                rt_index-=1
                rt_height=heights[rt_index]
            temp_area=(rt_index-lt_index)*min(lt_height,rt_height)
            area=max(area,temp_area)
        return area