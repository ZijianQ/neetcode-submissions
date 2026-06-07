class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs( i, cur, total):
            if total == target:
                res.append(cur)
                return

            if i >= len(candidates) or total > target:
                return

            dfs( i+1, cur + [candidates[i]], total + candidates[i])

            while i+1 < len(candidates) and candidates[i] ==candidates[i+1]:
                i +=1

            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res
        