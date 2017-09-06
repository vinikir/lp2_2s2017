# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  q = len(s)
  if q == 2:
    r = s[0:2]*3
  elif q == 5:
    r = s[3:5]*3 
  else:
    r = s[2:4]*3   
  return r

def test_ex07():
  print ('Extra End')
  assert extra_end('Hello') == 'lololo'
  assert extra_end('ab') == 'ababab'
  assert extra_end('Hi') == 'HiHiHi'
  assert extra_end('Candy') == 'dydydy'
  assert extra_end('Code') == 'dedede'

