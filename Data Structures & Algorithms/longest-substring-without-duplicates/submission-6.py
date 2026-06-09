class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        
        freq={}
        last_index=0
        pres_array=[]
        max_size=0
        temp_size=0
        for i in range(len(s)):
            print(s[i],freq,pres_array)
            if s[i] in freq:
                max_size=max(max_size,len(pres_array))
                # print(pres_array[last_index], s[i])
                flag=True
                while flag and (pres_array[last_index]!=s[i] or pres_array[last_index]==s[i]) :
                    if pres_array[last_index]==s[i]:
                        flag=False
                    # print('----',pres_array[last_index],pres_array,freq,flag)
                    del freq[pres_array[last_index]]
                    pres_array.pop(0)
                    # last_index+=1
                    # print(pres_array)
                    # print(freq,pres_array)
                    if len(pres_array)==1:
                        break
                if freq.get(s[i]):
                    pass
                else:
                    last_index=0
                    freq[s[i]]=1
                    pres_array.append(s[i])
            else:
                freq[s[i]]=1
                pres_array.append(s[i])
                
        max_size=max(max_size,len(pres_array))
        # print(pres_array,max_size)
        # print('----------')
        return max_size
