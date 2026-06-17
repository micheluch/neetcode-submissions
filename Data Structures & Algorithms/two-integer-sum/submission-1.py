class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    result = [i, j]
                    break
            if result != []: break
        return result