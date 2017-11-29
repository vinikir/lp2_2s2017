class Aluno():
    def __init__(self, nome, celular, email, ra):
        self.nome = nome
        self.celular = celular
        self.email = email
        self.ra = ra

    def confirma_teste(self,ra,lista):
        if ra in lista:
            print('aluno ja fez o teste')
        if ra not in lista:
            print('aluno pode fazer o teste')

    def mostra_quem_fez(self,ra,lista):
        if ra in lista:
            print('aluno ja enviou a tarefa')
        res = input(' o aluno {} ja enviou a tarefa ? (s/n)'.format(self.nome))
        res.lower()
        if res == 's':
            print('aluno ja enviou a tarefa')
            if self.ra not in lista:
                lista.append(self.ra)
        elif res == 'n':
            print('aluno não enviou a tarefa')
            res = input('dejesa enviar agora ? \n (s/n)')
            res.lower()
            if res == 's':
                print('enviando tarefa...')
                if self.ra not in lista:
                    lista.append(self.ra)
            else:
                print('ok')

    def aviso(self,numero,maximo):
        if numero >= maximo:
            print('numero maximo ja estourado')
            print('mas será matriculado\n')

    def media_aluno(self,n1,n2):
        media = (n1 + n2)/2
        print('media do aluno {} é igual a :{}'.format(self.nome,media))