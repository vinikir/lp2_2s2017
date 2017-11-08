from triangulos import Triangulo

ladoA = int(input('digite o ladoA do triangulo : '))
ladoB = int(input('digite o ladoB do triangulo : '))
ladoC = int(input('digite o ladoC do triangulo : '))
triangulo = Triangulo(ladoA,ladoB,ladoC)
triangulo.calcular_prerimetro()
triangulo.getMaior()