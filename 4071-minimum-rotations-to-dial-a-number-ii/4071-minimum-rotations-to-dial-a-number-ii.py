class Solution:
    def minRotations(self, n, s):
        def dist(a, b):
            d = abs(int(a) - int(b))
            return min(d, 10 - d)

      
        total = dist('0', s[0])

        for i in range(1, n):
            total += dist(s[i - 1], s[i])

        ans = total

        
        ans = min(ans, total - dist('0', s[0]) + dist('0', s[-1]))

        
        for k in range(1, n):
            new_cost = total

            
            new_cost -= dist(s[k - 1], s[k])
            new_cost += dist(s[k - 1], s[-1])

            ans = min(ans, new_cost)

        return ans
        