class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []

        for current in intervals:
            if not res or res[-1][1] < current[0]:
                res.append(current)
            else:
                res[-1][1] = max(res[-1][1], current[1])
        return res