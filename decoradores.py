


# decoradores: funciones que a su vez añaden funcionalidades a otras funciones



def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):

        # acciones adicionales que decoran..
        print('vamos a realizar un calculo : ')

        funcion_parametro(*args, **kwargs)

        # acciones adicionales que decoran ...
        print('hemos terminado el calculo  ')

    return funcion_interior

@funcion_decoradora
def suma(num1,num2,num3):
    print(num1 +  num2 + num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1 -  num2)



@funcion_decoradora
def expo(base, exponente):
    print(pow(base,exponente))

suma(10,20,20)
resta(200,230)
expo(5,3)

print('hola mundo')