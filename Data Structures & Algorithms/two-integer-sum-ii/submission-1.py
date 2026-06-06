class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq={}
        res=[]
        count=1
        for i in numbers:
            if i in freq:
                pass
            else:
                freq[i]=count
            count+=1
        # print(freq)

        for i in freq.keys():
            # print(i,'---------')
            if target-i in freq:
                # print(i)
                return [freq.get(i),freq.get(target-i)]
                