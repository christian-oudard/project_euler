limit = 100
nums = list(range(1, limit + 1))
print(sum(nums) ** 2 - sum(n ** 2 for n in nums))
