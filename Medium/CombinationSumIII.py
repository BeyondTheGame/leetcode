class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [x for x in range(1, 10)]
        self.res = []
        self.helper(candidates, n, [], k, 0)
        return self.res

    def helper(self, candidates, target, out, count, start):
        if target == 0 and len(out) == count:
            self.res.append(out[:])
            return
        elif target > 0 and len(out) < count:
            for index in range(start, len(candidates)):
                target -= candidates[index]
                out.append(candidates[index])
                self.helper(candidates, target, out, count, index+1)
                target += candidates[index]
                out.pop()


k =3
n= 7
s =Solution()
res = s.combinationSum3(k ,n)
print(res)