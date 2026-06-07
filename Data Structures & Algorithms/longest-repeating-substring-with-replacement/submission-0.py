class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxFreq = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1
            maxFreq = max(maxFreq, count[c])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
