#!/usr/bin/env python3

class perro():
    
    def __init__(self, nombre, hrs_dsp_beber, reloj, pasear):
        self.nombre = nombre
        self.hrs_dsp_beber = hrs_dsp_beber
        self.reloj = reloj
        self.pasear = pasear
    
    # permite especificar el tiempo (horas) con un numero
    # recibe un int de argumento 
    def set_tomar_agua(self, tomar_agua):

        # perro toma agua solo bajo la siguiente condicion
        if tomar_agua == 1 and self.pasear is not True:
            self.hrs_dsp_beber = 0
            print(f"{self.nombre} bebio agua a las {self.reloj} hrs.")

        # circunstancias en que perro no toma agua
        else:
            # si perro salio a pasear, tal que no debe tomar agua
            if tomar_agua == 1 and self.pasear is True:
                print(f"Accion no disponible, {self.nombre} aun esta paseando tal que no debe tomar agua.")
                # se asigna booliano 'False' para accion en siguiente ciclo
                self.pasear = False
            # si perro no toma agua ni pasea 
            else:
                pass

            """accion general para ambos casos anteriores """
            # se aumenta una hora desde ultima vez que perro bebio agua
            self.hrs_dsp_beber += 1
            print(f"{self.nombre} bebio agua hace {self.hrs_dsp_beber} hora(s).")

    # retorna hrs (int) pasadas desde que perro bebio agua y si perro esta paseando (T or F)
    def get_hora_toma_agua(self):
        return self.hrs_dsp_beber, self.pasear

    # indicara si el perro necesita salir a pasear
    def caminar(self, solicitud):
        
        # dirigue a ultimo caso de metodo, tal que indica ultima vez que perro bebio
        self.set_tomar_agua(0)

        if self.hrs_dsp_beber < 4 and solicitud is False:
            pass
        elif self.hrs_dsp_beber < 4 and solicitud is True:
            print(f"Accion no disponible, {self.nombre} bebio agua hace menos de 4 hrs.")
        elif self.hrs_dsp_beber >= 4 and solicitud is False:
            print(f"Advertencia, {self.nombre} ya debe salir a pasear.")
        else:
            print(f"{self.nombre} sale a pasear.")
            self.pasear = True


nombre_perro = input("Bienvenid@, por favor ingrese nombre de perro.\n")
reloj = 0
hrs_dsp_beber = 4
caminar = None
n = None

while n != 0:

    print(f"\nEl reloj marca las {reloj} (hrs).")

    print("Menu")
    print(f"Marque <1> si {nombre_perro} toma agua")
    print(f"Marque <2> si {nombre_perro} sale a pasear")
    print(f"Marque <3> si {nombre_perro} no hace ninguna de las acciones anteriores")
    print("Marque <0> para salir de menu.")
    n = int(input(">"))
    
    Perro = perro(nombre_perro, hrs_dsp_beber, reloj, caminar)

    # perro toma agua
    if n == 1:
        # 1 = True  tal que se obedece argumento tipo 'int' solicitado en ejercicio
        tomar_agua = 1
        Perro.set_tomar_agua(tomar_agua)
    # perro sale a pasear
    elif n == 2:
        Perro.caminar(True)
    # perro no hace ninguna actividad de las ya mencionadas
    # tiempo continua avanzando
    elif n == 3:
        Perro.caminar(False)
    else:
        pass
    
    # se asignan nuevos valores para actualizar atributos en siguiente ciclo
    hrs_dsp_beber, caminar = Perro.get_hora_toma_agua()

    reloj += 1
        
