def lucky_sum(a, b, c):
  nums = list()
  nums.append(a)
  nums.append(b)
  nums.append(c)
  summ = 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      break
    summ += nums[i]
  return summ