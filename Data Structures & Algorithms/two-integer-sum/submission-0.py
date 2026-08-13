class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            find = target - value
            if find in seen:
                return [seen[find], key]
            seen[value] = key
        return []