# Problem: Two Sum - https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums): # i = 0 n = 2, target = 9, 9 - 2 = 7, 7 is not in seen so we add seen[n] = i seen{ 2: 0}
        dif = target - n
        if dif in seen:
            return [seen[dif], i]
        seen[n] = i

print(twoSum([2,7,11,15], 9))