class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = r = 0
        l_max = [0] * n
        r_max = [0] * n
        for i in range(n):
            j = -i - 1
            l_max[i] = l
            r_max[j] = r
            l = max(l, height[i])
            r = max(r, height[j])
        summ = 0    
        for i in range(n):
            pot = min(l_max[i], r_max[i])
            summ += max(0, pot - height[i])
        return summ
