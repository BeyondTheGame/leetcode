class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        从后向前扫描
        """
        if m == 0 or n == 0:
            return
        count1, count2 = 0, 0
        insert_count = 0    # 记录num2中有多少个数据插入了num1
        while count1 < m and count2 < n:
            if nums1[m-1-count1] < nums2[n-1-count2]:
                nums1[m+n-1-insert_count] = nums2[n-1-count2]
                count2 += 1
            else:
                nums1[m + n - 1 - insert_count] = nums1[m - 1 - count1]
                count1 += 1
            insert_count += 1
        if count2 >= n:
            return
        else:
            while count2 < n:
                nums1[m+n-1-insert_count] = nums2[n-1-count2]
                count2 += 1
                insert_count += 1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)[:]

    def merge3(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

    def merge4(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        return


solution = Solution()
num1 = [1, 2, 3]
num2 = [2, 5, 6]
solution.merge(num1, len(num1), num2. len(num2))
