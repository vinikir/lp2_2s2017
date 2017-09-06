
def alarm_clock(day, vacation):
  if vacation == True:
    if day == 0 or day == 6:
      res = 'off'
    else:
      res = '10:00'
  else:
    if day == 0 or day == 6:
      res = '10:00'
    else:
      res = '7:00'        
  return res