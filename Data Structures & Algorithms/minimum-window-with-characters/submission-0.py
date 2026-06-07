class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        need = {}
        for c in t:
            need[c] = need.get(c,0)+1

        window = {}
        need_len= len(need)
        have = 0
        
        res = []
        res_len= float("inf")
        l =0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) +1
            if c in need and need[c]== window[c]:
                have += 1

            while have == need_len :
                if r-l+1 < res_len :
                    res = [l , r ]
                    res_len = r -l +1
                extra = s[l]
                window[extra]-=1
                if extra in need and window[extra] < need[extra]:
                    have -=1
                l+=1
       

        if res_len == float("inf"):
            return ""

        l, r = res
        return s[l:r+1]
                
