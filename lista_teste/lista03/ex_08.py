def squirrel_play(temp, is_summer):

  if is_summer == True:
    if temp >= 60 and temp <= 100:
      res=True
    else:
      res=False  
  else:
    if temp >= 60 and temp <= 90:
     res=True
    else:
     res=False 
      
  return res