
class Areas:
    #esta clase calcula las areas de las figuras geometricas

    def cuadrado(self,lado):
        """
            calcula el area de un cuadrado, elevando el lado al cuadrado
        """
        return 'el area del cuadrado es : ' + str(lado*lado)

    def areaTriangulo(self, base,altura):
        return 'el area del triangulo es  : ' + str((base*altura)/2)


help(Areas)