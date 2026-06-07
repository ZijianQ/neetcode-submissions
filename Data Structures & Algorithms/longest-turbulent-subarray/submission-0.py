class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1: return 1

        L = 0

        total = arr[0]

        res =1


        for R in range(len(arr)):
            if arr[R] == arr[R-1]: 
                L =R
            elif R ==1 or (arr[R] -arr[R-1])* (arr[R-1]- arr[R-2]) > 0:
                L = R-1

            res = max(res, R - L +1)

        return res
            
            
        