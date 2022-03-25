
#from _typeshed import Self


#permite especificar el tiempo (horas) con un umero entero -> ¿timepo de que?
#devuelve la hora de en que bebio agua el perro  -> ingresa hora a sacar a pasear
#verdadero (True) indicara si el perro necesita salir a pasear  -> ¿necesita el perro orinar?

class perro():

    def __init__(self):
        self.pasear = None
        self.tomar_agua = None
        #self.hrs_para_pasear = None


    def set_tomar_agua(self, perro_toma_agua, hrs_para_pasear):
        
        # si perro toma agua
        if perro_toma_agua is True:
            # cuenta para que perro pueda pasear : '0' = ok
            hrs_para_pasear = -4
        else:
            hrs_para_pasear = hrs_para_pasear + 1
            pass
        
        #print("las horas para salir a pasear son ", hrs_para_pasear* -1)
        return hrs_para_pasear

        
    #devuelve la hora de en que bebio agua el perro
    def get_hora_toma_agua(self, hrs_para_pasear):

        print(f"El perro bebio agua hace {hrs_para_pasear + 4} hrs.")

        return hrs_para_pasear

    #verdadero (True) indicara si el perro necesita salir a pasear
    def caminar(self, hrs_para_pasear):

        print("las horas para salir a pasear son ", hrs_para_pasear)

        if hrs_para_pasear < 0:
            self.pasear is False
            hrs_para_pasear += 1
            print("Perro no ha superado las 4 hrs despues de tomar agua. No saldra a pasear")
        else:
            self.pasear is True
            print("Perro sale a pasear")
            #hrs_para_pasear = -4

        return hrs_para_pasear


n = None
horas_para_pasear = 0

while n != 0:

    print("Menu")
    print("Marque <1> si perro toma agua")
    print("Marque <2> si perro sale a pasear")
    print("Marque <3> si perro no hace nada")
    print("Marque <0> para salir de programa.")
    n = int(input())

    Perro = perro()

    # perro toma agua
    if n == 1:
        # se drigue a metodo
        horas_para_pasear = Perro.set_tomar_agua(True, horas_para_pasear)
        horas_para_pasear = Perro.get_hora_toma_agua(horas_para_pasear)
    # perro sale a pasear
    elif n == 2:
        horas_para_pasear = Perro.caminar(horas_para_pasear)
    else:
        horas_para_pasear = Perro.set_tomar_agua(False, horas_para_pasear)
        pass

    print(f"quedan {horas_para_pasear * -1} hrs para sacar a pasear a perro")
        





