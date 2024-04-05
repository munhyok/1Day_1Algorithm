class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        setNums = set(nums)

        if len(setNums) == len(nums):
            return False
        else: return True