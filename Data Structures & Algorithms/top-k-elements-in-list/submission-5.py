class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for n in nums:
            count[n] +=1

        vur = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            vur[cnt] .append(n)

        res =[]
        for i in range(len(vur)-1,0,-1):
            for n in vur[i]:
                res.append(n)
                if len(res)== k:
                    return res



        