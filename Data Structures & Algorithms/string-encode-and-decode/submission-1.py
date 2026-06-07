class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        size = []
        for s in strs:
            size.append(len(s))
        for sz in size:
            res+= str(sz)
            res += ','
        res +='#'
        for s in strs:
            res +=s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return[]
        res, i = [],0   

        size =[]
        while s[i]!= '#':
            med = ""
            while s[i] != ',':
                med += s[i]
                i +=1
            size.append(int(med))
            i +=1
        i +=1

        for sz in size:
            res.append(s[i: i+sz])
            i +=sz
        
        return res




            




