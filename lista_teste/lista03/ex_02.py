def same_first_last(nums):
  t =len(nums)
  if t > 0:
    pri = nums[0]
    ult = nums[-1]
    if pri == ult:
      res = True
    else:
      res = False 
  else:
    res = False     
  return res