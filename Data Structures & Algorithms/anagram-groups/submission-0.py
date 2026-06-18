class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        result = []
        for item in strs:
            x = ''.join(sorted(item))
            if x not in sorted_strs:
                sorted_strs[x] = [item]
            else:
                sorted_strs[x].append(item)
        for key in sorted_strs:
            result.append(sorted_strs[key])
        return result