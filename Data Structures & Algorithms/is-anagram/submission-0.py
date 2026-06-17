class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # no point checking
            return False

        counts = {}
        for ch in s:
            if counts.get(ch) != None:
                counts[ch][0] += 1
            else:
                counts[ch] = [1, 0]
        for ch in t:
            if counts.get(ch) != None:
                counts[ch][1] += 1
            else:
                counts[ch] = [0, 1]
        for ch in counts:
            if counts[ch][0] != counts[ch][1]:
                return False
        return True

        