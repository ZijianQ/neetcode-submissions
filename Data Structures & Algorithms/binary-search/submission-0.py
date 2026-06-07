class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        n = len(nums)
        

        l, r = 0 , n

        while l < r:
            m = l + ((r - l) // 2)

            if target <= nums[m]:
                r =m
            else:
                l = m+1
        return l  if (l < len(nums) and nums[l] == target) else -1

        
        