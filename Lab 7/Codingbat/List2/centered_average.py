def centered_average(nums):
  cnt1 = 0
  cnt2 = 0
  summ = 0
  for i in nums:
    if i == min(nums) and cnt1 == 0:
      cnt1 += 1
      continue
    if i == max(nums) and cnt2 == 0:
      cnt2 += 1
      continue
    summ += i
  return summ / (len(nums) - 2)