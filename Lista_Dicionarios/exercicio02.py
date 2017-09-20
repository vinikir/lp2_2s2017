#Exercicio 2 
#Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
#quantidade em um dicionário, onde a chave é a vogal considerada. Escreva um
#programa para testar a função.
def textolino_02(t):     
 a = t.count('a')
 e = t.count('e')
 i = t.count('i')
 o = t.count('o')
 u = t.count('u')
 dicionario = {
   'a': a,
   'e': e,
   'i': i,
   'o': o,
   'u': u,
 }
 return dicionario 