#Exercicio 2 
#Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
#quantidade em um dicionário, onde a chave é a vogal considerada. Escreva um
#programa para testar a função.
from exercicio02 import textolino_02

def test_02():
  print ('Texto')
  assert textolino_02('Maravilhas do mundo eu') == {'a':3,'e':1,'i':1,'o':2,'u':2}
  assert textolino_02('kaio bonitao') == {'a':2,'e':0,'i':2,'o':3,'u':0}
 