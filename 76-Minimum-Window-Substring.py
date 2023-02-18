class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        mx = float("inf")
        output = ""
        start, end = 0, 0
        count = len(lookup)
        
        while end < len(s):
            
            # End pointer
            while end < len(s) and count != 0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -=1
                end += 1
                
            # Start pointer
            while start <= end and count == 0:             
                if end - start < mx:
                    mx = end - start
                    output = s[start:end]
                
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]] > 0:
                        count += 1            
                start += 1
        
        return output
