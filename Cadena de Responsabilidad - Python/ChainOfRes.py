#!/usr/bin/env python
# -*- coding: latin-1 -*-

class Manejador:

    def __init__(self):
        self._sucesor = 0 
    
    def get_sucesor(self):
        getattr(self,"_sucesor")
    def set_sucesor(self,sucesor):
        setattr(self,"_sucesor",sucesor)
    def manejador_operacion(self,op):
        pass
    


class ManejadorNomina(Manejador):

    def manejador_operacion(self,op):
        if op == 1:
            print("Liquidando por nómina")
        else:
            self._sucesor.manejador_operacion(op)

class ManejadorHoraCatedra(Manejador):

    def manejador_operacion(self,op):
        if op == 2:
            print("Liquidando por Hora Cátedra")
        else:
            self._sucesor.manejador_operacion(op)

class ManejadorSalario(Manejador):

    def manejador_operacion(self,op):
        if op == 3:
            print("Liquidando por Salario")
        else:
            self._sucesor.manejador_operacion(op)

class ManejadorHonorario(Manejador):

    def manejador_operacion(self,op):
        if op == 4:
            print("Liquidando por Hononario")
        else:
            self._sucesor.manejador_operacion(op)

class ManejadorDocPlanta(Manejador):

    def manejador_operacion(self,op):
        if op == 5:
            print("Liquidando Docente de Planta")
        else:
            self._sucesor.manejador_operacion(op)

class ManejadorDef(Manejador):

    def manejador_operacion(self,op):
        print("No es una opción válida")

class Ejemplo:
    
    def main(self,op):
        manejadores = []
        maneUno = ManejadorNomina()
        maneDos = ManejadorHoraCatedra()
        maneTres = ManejadorSalario()
        maneCuatro = ManejadorHonorario()
        maneCinco = ManejadorDocPlanta()
        maneSeis = ManejadorDef()

        manejadores.append(maneUno)
        manejadores.append(maneDos)
        manejadores.append(maneTres)
        manejadores.append(maneCuatro)
        manejadores.append(maneCinco)
        manejadores.append(maneSeis)

        for i in range (0,len(manejadores)-1):
            manejadores[i].set_sucesor(manejadores[i+1])

        manejadores[0].manejador_operacion(op)



if __name__ == "__main__":
    print("Ingrese un numero para liquidar un tipo de empleado")
    print("1)Nómina\n2)Hora Cátedra\n3)Salario\n4)Honorario\n5)Docente de planta")

    opcion = int(input("Ingrese una opción: "))
    ejemplo = Ejemplo()
    ejemplo.main(opcion)
    
