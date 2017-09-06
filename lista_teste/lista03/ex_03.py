def common_end(a, b):
  res=True
  pri_a = a[0]
  pri_b = b[0]
  ult_a = a[-1]
  ult_b = b[-1]
  if pri_a == pri_b:
    res= True
  elif ult_a == ult_b:
    res= True
  else:
    res=False
  return  res
