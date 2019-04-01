"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.helper(candidates, target, [], 0)
        return self.res

    def helper(self, candidates, targets, out, start):     # 调用一次helper进入一个level
        if targets == 0:
            self.res.append(out[:])
            return
        elif targets < 0:
            return
        else:
            for index in range(start, len(candidates)):
                out.append(candidates[index])
                targets -= candidates[index]
                self.helper(candidates, targets, out, index)
                targets += candidates[index]
                out.pop()