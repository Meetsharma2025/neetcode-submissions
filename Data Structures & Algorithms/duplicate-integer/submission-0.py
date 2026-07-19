class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if (i not in d):
                d[i] = i

            elif (i in d):
                return True
        return False