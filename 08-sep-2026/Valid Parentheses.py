# Problem: Longest Common Prefix - https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    stack = []

    pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for character in s:

        if character in pairs:
            stack.append(character)

        else:
            if not stack:
                return False

            if pairs[stack[-1]] != character:
                return False

            stack.pop()

    return len(stack) == 0
print(isValid("{]"))