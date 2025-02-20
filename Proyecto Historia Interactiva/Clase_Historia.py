class Historia:
    historia : str = []
    opciones : str = []
    puntero : int
    matriz_hist_op : int = ()
    def __init__(self):
        self.puntero = 0
        self.opciones = ["Tomar el camino de la izquierda", "Tomar el camino de la derecha", "Avanzar", "Atacar"]
        
        self.historia = ["Bienvenido Aventurero, te encuentras en una Adea en un valle", 
                         "Has llegado a la mina donde hay metales preciosos.", 
                         "Has llegado al rio en donde hay un puente colgante", 
                         "Has llegado a una cueva en donde hay un TROL PELIGROSO!", 
                         "Los aldeanos te han matado por atacarlos",
                         "El TROL te ha matado",
                         "Has matado al TROL y te has quedado con su botín, Felicidades!",
                         "Has cruzado el puente colgante y te encuentras con Bandidos",
                         "Los Bandidos te han matado", 
                         "Has matado a los Bandidos y te quedas con su botín!, Felicidades!",
                         "Te has echo RICO, Felicidades!", 
                         "Has llegado a un bosque oscuro, no ves nada, te pierdes, has muerto",
                         "Has llegado a una Gran Ciudad, te conviertes en un gran aventurero!"]
        self.matriz_hist_op = {(0,1): 1, (0,2): 2, (0,3): 3, (0,4): 4, (1,1): 2, (1,2): 3, (1,3): 10, (1,4): 4, (2,1): 3, (2,2): 1, (2,3): 12, (2,4): 4, (3,1): 1, (3,2): 7, (3,3): 1, (3,4): 5, (7,1): 11, (7,2): 12, (7,3): 6, (7,4): 9}

    def mostrar(self) -> bool:
        print(self.historia[self.puntero])
        if self.puntero == 4 or self.puntero == 5 or self.puntero == 6 or self.puntero == 8 or self.puntero == 9 or self.puntero == 10 or self.puntero == 11 or self.puntero == 12:
                print("Fin del Juego")
                return True
        print("Opciones:")
        for i in range(len(self.opciones)):
            print(f"{str(i+1)}- {self.opciones[i]}")
        return False

    def elegir_opcion(self, opcion):
        # print("Puntero anterior: " + str(self.puntero))
        # print("Opción elegida: " + str(opcion))
        if 0 <= opcion < len(self.opciones)+1:
            temp = self.matriz_hist_op[self.puntero, opcion]
            self.puntero = temp
            print(str(self.puntero))
        else:
            print("Opción no válida")
        # print("Nuevo Puntero: " + str(self.puntero))
        
