class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        result = True
        while left < right:
            if not s[left].isalnum():
                right += 1
                pass
            elif not s[right].isalnum():
                left -= 1
                pass
            elif s[left] != s[right]:
                result = False
                print("%s is not %s" % (s[left], s[right]))
                break
            left += 1
            right -= 1
        return result