class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_string={}

        for anterata in strs:
            
            temp =anterata
            # print(temp)
            temp_list=[0]*26
            temp_final=[]
            for k in temp:
                # print(ord(k)-ord('a'))
                temp_list[ord(k)-ord('a')]+=1
            # print(temp_list)

            temp=''
            for i in range(len(temp_list)):
                temp=temp+str(temp_list[i])
                temp=temp+(chr(i+ord('a')))
            # print(temp)
            if temp in freq_string:
                freq_string[temp].append(anterata)
            else:
                freq_string[temp]=[anterata]

        res=[]
        for i in freq_string:
            res.append(freq_string[i])

        return res