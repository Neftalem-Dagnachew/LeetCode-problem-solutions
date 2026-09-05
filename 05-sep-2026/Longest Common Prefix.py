# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(*strs):
    prifix = ""
    leest = list(strs)
    for i in range(len(leest[0])):
        for s in leest:
            if i >= len(s) or leest[0][i] != s[i]:
                return prifix

        prifix += leest[0][i]

    return prifix

print(longestCommonPrefix("flower", "flow", "flighe"))

# leest[0] = flower  
# i = 0 - f
# i = 1 - l
# i = 2 - o
# i = 3 - w
# i = 4 - e
# i = 5 - r