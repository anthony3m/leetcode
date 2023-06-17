class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        result = [1] * len(ratings)
        
        # Left to right
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                result[i] = max(result[i], result[i-1] + 1)
        
        # Right to left
        for i in reversed(range(0, len(ratings) - 1)):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)
        
        
        return sum(result)