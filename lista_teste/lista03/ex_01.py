def first_last6(nums):
  retorno = True
  if not 6 in nums:
     retorno = False
  else:
    if nums[0] == 6 or nums[-1] == 6:
      retorno = True
    else:
      retorno = False
  return retorno