def date_fashion(eu, par):
  if eu <=2 or par <=2:
    res=0
  elif eu >=8 or par >=8:
    res=2
  else:
    res=1   
  return res