def alarm_clock(day, vacation):
  if vacation:
    if day in [1, 2, 3, 4, 5]:
      return '10:00'
    else:
      return 'off'
  else:
    if day in [1, 2, 3, 4, 5]:
      return '7:00'
    else:
      return '10:00'