class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}
        for i,val in enumerate(nums):
            indx[val] = i
        for i,val in enumerate(nums):
            left = target-nums[i]
            if(left in indx and i != indx[left]):
                return [i,indx[left]]