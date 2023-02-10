class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_chars = {}
        for char in s:
            if dict_chars.get(char):
                dict_chars[char] += 1
            else:
                dict_chars[char] = 1
        res = 0
        already_mid_populate = False
        for num_chars in dict_chars.values():
            if num_chars % 2 != 0:
                if already_mid_populate:
                    res += num_chars - 1
                else:
                    res += num_chars
                    already_mid_populate = True
            else:
                res += num_chars
        return res


s = "abccccdd"
sol = Solution()
print(sol.longestPalindrome(s))
