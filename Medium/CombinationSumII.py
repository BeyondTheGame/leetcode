class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.res = []
        self.helper(candidates, target, [], 0)
        return self.res

    def helper(self, candidates, target, out, start):
        if target < 0:
            return
        elif target == 0:
            self.res.append(out[:])
        else:
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]:
                    continue
                target -= candidates[index]
                out.append(candidates[index])
                self.helper(candidates, target, out, index+1)
                target += candidates[index]
                out.pop()