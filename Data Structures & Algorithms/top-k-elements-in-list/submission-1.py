class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        return [pair[0] for pair in frequency.most_common(k)]