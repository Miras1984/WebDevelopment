def xyz_there(str):
  cnt = 0
  for i in range(0, len(str) - 2):
    if str[i] + str[i + 1] + str[i + 2] == 'xyz' and str[i - 1] != '.':
      cnt += 1
  return cnt > 0