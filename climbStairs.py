from itertools import permutations


class Solution(object):
    #     def climbStairs(self, n):
    #         a, b = 1, 1
    #         for i in range(n):
    #             a, b = b, a + b
    #         return a

    def climbStairs(self, n):
        opt = [0, 1, 2] + [0 for i in range(0, n)]
        for i in range(3, n + 1):
            opt[i] = opt[i - 1] + opt[i - 2]
        return opt[n]