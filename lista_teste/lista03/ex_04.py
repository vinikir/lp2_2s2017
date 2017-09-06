def maior_ponta(nums):
 pri_a= nums[0]
 ult_a= nums[-1]
 if pri_a > ult_a:
   res=[pri_a,pri_a,pri_a]
 elif pri_a < ult_a:
    res=[ult_a,ult_a,ult_a]
 else:
  res=[ult_a,ult_a,ult_a]

 return res