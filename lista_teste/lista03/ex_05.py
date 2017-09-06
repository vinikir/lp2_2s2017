def sum2(nums):
  t=len(nums)
  if t > 1: 
    pri=nums[0]
    ult=nums[1]
    res=pri+ult
  elif t == 1 :
    pri=nums[0]
    res=pri
  else:
    res = 0
  return res 