

from datetime import date, datetime

hoje = date.today()
b = str(input('escreve ai dd/mm/aaaa :\n'))
c = b.split('/')
d = date(int(c[2]),int(c[1]),int(c[0]))
if d > hoje:
   print("Data inválida, não pode ser aplicado antes da data de hoje")
else:
    print("Recebido com sucesso")

