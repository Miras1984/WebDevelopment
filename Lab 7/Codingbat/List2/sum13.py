def sum13(nums):
  summ = 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      if i == len(nums) - 1:
        continue
      nums[i + 1] = 0
      continue
    summ += nums[i]
  return summ