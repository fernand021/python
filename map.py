


def parImpar(num):

    if num % 2 ==0:
        return True

numeros = [1,2,3,4,5,6,7,7,8]
print(list(filter(parImpar, numeros)))

print('-----------------------------------------')

numero2 = [12,23,54,26,55,3,4,6,8]
print(list(filter(lambda numero_par : numero_par%2==0, numero2)))


class empleado():

    def __init__ (self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return '{} que trabaja como {} tiene un salario de {} €'.format(self.nombre, self.cargo, self.salario)

lista_empleados = [
    empleado('juan','director',74000),
    empleado('fernando','gerente general',1000000),
    empleado('ana','presidenta',30495)
] 



def calculoComision(empleado):
    if (empleado.salario <= 35000):
        empleado.salario = empleado.salario * 1.03
    return empleado

lista_empleadosComision = map(calculoComision, lista_empleados)

for empleado in lista_empleadosComision:
    print(empleado)