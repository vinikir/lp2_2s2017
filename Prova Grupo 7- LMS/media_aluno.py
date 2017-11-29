from alunos import Aluno

nome = input('digite o nome do aluno \n')
celular = 0000000
email = 'email@email.com'
ra = input('digite o R.A do aluno \n')
aluno = Aluno(nome,celular,email,ra)
n1 = int(input('digite a primeira nota  do aluno : \n'))
n2 = int(input('digite a segunda nota do aluno : \n'))
aluno.media_aluno(n1,n2)