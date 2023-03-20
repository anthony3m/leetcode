class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if sum(path) == target:
                res.append(path[:])
                return 
			
            if sum(path) > target:
                return 
			
            for x in range(i, len(candidates)):
                path.append(candidates[x])
                dfs(x, path)
                path.pop()

        dfs(0, [])
        return res
