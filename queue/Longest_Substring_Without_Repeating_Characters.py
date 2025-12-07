
"""

abcabcbb
output = 3 -> abc

pwwkew
output = 3 -> wke

"""


def lengthOfLongestSubstring(s: str):
    max_len = 0
    result = []
    for char in s:
        if char in result:
            index = result.index(char)
            result = result[index+1:]
        result.append(char)
        max_len = max(len(result), max_len)
    return max_len

print(lengthOfLongestSubstring("pwwkew"))