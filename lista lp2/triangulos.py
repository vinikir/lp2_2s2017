class Triangulo:
    def __init__(self,ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC


    def calcular_prerimetro(self):
        res = (self.ladoA+self.ladoB+self.ladoC)
        print('a área do seu triangulo é {}'.format(res))


    def getMaior(self):
        if(self.ladoA > self.ladoB) and (self.ladoA > self.ladoC):
            print('o ladoA do triangulo é maior')
        elif(self.ladoB > self.ladoA) and (self.ladoB > self.ladoC):
            print('o ladoB do triangulo é maior')
        elif(self.ladoC > self.ladoA) and (self.ladoC > self.ladoB):
            print('o ladoC do triangulo é maior')
        else:
            print('todos os lados são iguais')