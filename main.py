# 1-mashq
nums = [2, 7, 11, 15]
target = 9

d = {}
for i, n in enumerate(nums):
    if target - n in d:
        print([d[target - n], i])
    d[n] = i
# 2-mashq
s = "abcabcbb"

seen = set()
l = 0
max_len = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    max_len = max(max_len, r - l + 1)

print(max_len)
# 3-mashq
nums = [2,2,1,2,3,2,2]

count = 0
candidate = None

for n in nums:
    if count == 0:
        candidate = n
    count += (1 if n == candidate else -1)

print(candidate)
# 4-mashq
words = ["eat", "tea", "tan", "ate"]

d = {}
for w in words:
    key = "".join(sorted(w))
    d.setdefault(key, []).append(w)

print(list(d.values()))
# 5-mashq
nums = [1,2,3,4]

res = [1]*len(nums)

left = 1
for i in range(len(nums)):
    res[i] = left
    left *= nums[i]

right = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= right
    right *= nums[i]

print(res)
