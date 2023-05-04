class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       res = [0] * len(temperatures)
       stack = []  

       for i, curTemp in enumerate(temperatures):
           while stack and temperatures[stack[-1]] < curTemp:
               prevTemp = stack.pop()
               res[prevTemp] = i - prevTemp
           stack.append((i))
       return res