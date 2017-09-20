#O máximo divisor comum (MDC) entre dois números m e n pode ser calculado pelo
#algoritmo de Euclides. Começando com os valores m e n, a seguinte fórmula é
#aplicada repetidamente até que m seja 0:
#𝑛, 𝑚 = 𝑚, 𝑛 % 𝑚
#Quando m = 0, n é o MDC de m e n. Escreva em python:
#• Um programa com uma função que calcule o MDC de 2 números digitados pelo
#usuário.
#• Um programa para testar a função utilizando pytest
from exercicio01 import mdc

      
def test_01():
  print ('MDC')
  assert mdc(3,6) == 3 #resposta do bagui
  assert mdc(5,15) == 5
  assert mdc(7,14) == 7
