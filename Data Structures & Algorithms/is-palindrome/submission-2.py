import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        lf_index=0
        rt_index=len(s)-1
        while lf_index!=rt_index and lf_index < rt_index:
            print(lf_index,rt_index)
            if s[lf_index]!=s[rt_index]:
                return False
            lf_index+=1
            rt_index-=1
        return True