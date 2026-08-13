class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        output = []

        for string in strs:
            sorted_string = ''.join(sorted(string))
            seen[sorted_string].append(string)
        
        return list(seen.values())
        