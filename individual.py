import math
a = float(input('Введите длину меньшего основания трапеции: '))
b = float(input('Введите длину большего основания трапеции: '))
c = float(input('Введите угол при большем основании: '))
h = (b-a)/2*math.tan(c)
print('Площадь трапеции равна: ', ((a+b)/2)*h)