def sum67(nums):
  summ = 0
  for i in range(0, len(nums)):
    if nums[i] == 6:
      j = i
      while nums[j] != 7:
        nums[j] = 0
    summ += nums[i]
  return summ

