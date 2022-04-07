def no_teen_sum(a, b, c):
  if fix_teen(a): a = 0
  if fix_teen(b): b = 0
  if fix_teen(c): c = 0
  return a + b + c

def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return True
  return False