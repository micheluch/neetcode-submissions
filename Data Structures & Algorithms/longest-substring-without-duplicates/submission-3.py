class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        elif len(s) == 1: return 1
        l, r = 0, 1
        seen = {}
        seen[s[l]] = True
        max_length = 0
        while l < len(s) and r < len(s):
            length = r - l + 1
            if s[r] in seen:
                while l < len(s) and s[l] != s[r]:
                    seen.pop(s[l])
                    l += 1
                if l < len(s):
                    seen.pop(s[l])
                    l += 1
            else:
                seen[s[r]] = True
                max_length = length if length > max_length else max_length
                r += 1
            
        return max_length