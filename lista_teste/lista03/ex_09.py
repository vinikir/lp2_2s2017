def pego_correndo(speed, is_birthday):
  if is_birthday == True:
    if speed > 65 and speed <= 85:
      res = 1
    elif speed > 85:
      res=2
    else:
      res=0
  else:
    if speed > 60 and speed <= 80:
      res = 1
    elif speed > 80:
      res=2
    else:
      res=0    
  
  return res