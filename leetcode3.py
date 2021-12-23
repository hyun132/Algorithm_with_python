from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    chars = defaultdict(int)
    max_len = 0
    for r, ch in enumerate(s):
        if ch in chars.keys() and chars[ch] + 1 > l:
            l = chars[ch] + 1
        else:
            max_len = max(max_len, r - l + 1)
        chars[ch] = r
    return max_len


# print(lengthOfLongestSubstring("abcabcbb")) #3
# print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("bbbb"))
