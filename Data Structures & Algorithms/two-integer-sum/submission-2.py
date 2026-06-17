class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen_diffs = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            complement = seen_diffs.get(nums[i])
            if complement == None:
                seen_diffs[diff] = i
            else:
                result = [complement, i] # since complement has to be an earlier index
                break
        return result