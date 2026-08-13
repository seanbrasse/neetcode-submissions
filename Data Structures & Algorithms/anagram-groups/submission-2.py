class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output = []
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in seen:
                seen[sortedString].append(string)
            else:
                seen[sortedString] = [string]
        for i in seen:
            output.append(seen.get(i))
        return output

        