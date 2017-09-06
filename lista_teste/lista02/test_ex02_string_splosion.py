# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  quant = len(s)  
  if quant == 6:
     stri = s[0:1] + s[0:2] + s[0:3] + s[0:4] + s[0:5] + s[0:6]
  elif quant == 5:
    stri = s[0:1] + s[0:2] + s[0:3] + s[0:4] + s[0:5]
  elif quant == 4:
   stri = s[0:1] + s[0:2] + s[0:3] + s[0:4] 
  elif quant ==3:
    stri = s[0:1] + s[0:2] + s[0:3]
  elif quant == 2:
    stri = s[0:1] + s[0:2] 
  elif quant == 1:
    stri = s[0:1] 
  
  return stri

def test_ex02():
  print ('String Explosion')
  assert string_splosion('Code') == 'CCoCodCode'
  assert string_splosion('abc') == 'aababc'
  assert string_splosion('ab') == 'aab'
  assert string_splosion('x') == 'x'
  assert string_splosion('fade') == 'ffafadfade'
  assert string_splosion('There') == 'TThTheTherThere'
  assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
  assert string_splosion('Bye') == 'BByBye'
  assert string_splosion('Good') == 'GGoGooGood'
  assert string_splosion('Bad') == 'BBaBad'
