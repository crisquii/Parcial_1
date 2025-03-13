class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = data
        
# Clases Listas Simplemente Enlazadas
class ListaCDE:
    def __init__(self):
        self.cabeza = None
    
    def vacio(self):
        if self.cabeza == None:
            print("No hay ninguna parada")
        else:
            print("Se encuentran paradas") 
            
    def contar(self):
        contador: 0
        control = self.cabeza
        while control == None:
            contador += 1
            control = control.siguiente
        print(f"Hay un total de {contador} paradas")
    
    def imprimir(self):
        control = self.cabeza
        print(f"La parada {control.data}")
        while control == None:
            control = control.siguiente
            print(f"La parada {control.data}")
            
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        
    def busqueda(self, dato):
        control = self.cabeza
        contador = 1 
        while control.data == dato or control == None:
            contador += 1
            control = control.siguiente
        if(control == None):
            print("La parada no se encunetra en la lista")
        else:
            print(f"La parada se encuentra en la posicion {contador}")