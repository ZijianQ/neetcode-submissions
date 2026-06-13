class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        total = 0
        res = []
        for i in digits:
            total += i * (10**n)
            n-=1
        total +=1

        for c in str(total):
            res.append(int(c))

        return res

        