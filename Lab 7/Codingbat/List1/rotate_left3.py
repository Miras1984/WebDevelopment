def rotate_left3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  nums[0] = b
  nums[1] = c
  nums[2] = a
  return nums