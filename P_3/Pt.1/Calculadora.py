class Calculadora_python:

    #Definimos los valores fijos de la calculadora
    def __init__(self, ent=25, flt=1.15, db=3.141592):
        self.entero= ent
        self.flotante= flt
        self.double= db
    
    #Definimos la operacion de suma para cualquier tipo de dato
    def Suma(self, a, b):
        return a+b
    
    #Definimos la operacion de resta para cualquier tipo de dato
    def Resta(self, a, b):
        return a-b
    
    #Definimos la operacion de multiplicacion para cualquier tipo de dato
    def Multiplicacion(self, a, b):
        return a*b
    
    #Definimos la operacion de division para cualquier tipo de dato
    def Division(self, a, b):
        return a/b
    
    #Definimos la operacion de modulo para cualquier tipo de dato
    def Modulo(self, a, b):
        Cociente= self.Division(a, b)
        Residuo= self.Resta(a, self.Multiplicacion(Cociente, b))
        return Residuo
    
    #Definimos la funcion que mostrara los valores precargados en la calculadora
    def mostrar_valores(self):
        print("Valores definidos en la Calculadora:")
        print(f"Entero: {self.entero}")
        print(f"Flotante: {self.flotante}")
        print(f"Double: {self.double}")
    
def main():
    
    #Creamos una instancia que llama a nuestra calculadora
    calc = Calculadora_python()

    #Mostramos los valores precargados en la calculadora
    calc.mostrar_valores()

    '''
        Ingresamos 6 datos diferentes a nuestra calculadora:
        a, b: Enteros
        c, d: Flotantes
        e, f: Doubles
    '''
    a = 18
    b = 9
    c = 7.5
    d = 2.5
    e = 12.0003
    f = 4.0001

    #Realizamos algunas operaciones con los enteros ingresados
    print(f"Suma de enteros {a} y {b}: {calc.Suma(a, b)}")
    print(f"Resta de enteros {a} y {b}: {calc.Resta(a, b)}")
    print(f"Multiplicacion de enteros {a} y {b}: {calc.Multiplicacion(a, b)}")
    print(f"División de enteros {a} y {b}: {calc.Division(a, b)}")
    print(f"Módulo de enteros {a} y {b}: {calc.Modulo(a, b)}")
    
    #Realizamos algunas operaciones con los flotantes ingresados
    print(f"Suma de flotantes {c} y {d}: {calc.Suma(c, d)}")
    print(f"Resta de flotantes {c} y {d}: {calc.Resta(c, d)}")
    print(f"Multiplicacion de flotantes {c} y {d}: {calc.Multiplicacion(c, d)}")
    print(f"División de flotantes {c} y {d}: {calc.Division(c, d)}")
    print(f"Módulo de flotantes {c} y {d}: {calc.Modulo(c, d)}")
    
    #Realizamos algunas operaciones con los doubles ingresados
    print(f"Suma de doubles {e} y {f}: {calc.Suma(e, f)}")
    print(f"Resta de doubles {e} y {f}: {calc.Resta(e, f)}")
    print(f"Multiplicacion de doubles {e} y {f}: {calc.Multiplicacion(e, f)}")
    print(f"División de doubles {e} y {f}: {calc.Division(e, f)}")
    print(f"Módulo de flotantes {e} y {f}: {calc.Modulo(e, f)}")

if __name__ == "__main__":
    main()