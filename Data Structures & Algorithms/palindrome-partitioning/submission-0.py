class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(j):
            if j == len(s):
                res.append(part.copy())
                return

            for i in range(j, len(s)):
                if self.valid(s, j, i):
                    part.append(s[j:i+1])
                    dfs(i + 1)
                    part.pop()

        dfs(0)
        return res

    def valid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

            
        