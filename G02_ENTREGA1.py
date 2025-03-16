class Nodo:
    def __init__(self, data):
        self.data = data # O(1)
        self.siguiente = None # O(1)

class ListaParadas:
    def __init__(self):
        self.cabeza = None # O(1)
    
    def vacio(self):
        if self.cabeza is None: # O(1)
            print("No hay ninguna parada") # O(1)
        else:
            print("Se encuentran paradas") # O(1)
    
    def contar(self):
        contador = 0 # O(1)
        control = self.cabeza # O(1)
        while control != None: # O(n)
            contador += 1 # O(1)
            control = control.siguiente # O(1)
        print(f"Hay un total de {contador} paradas") # O(1)
    
    def imprimir(self):
        control = self.cabeza # O(1)
        if control == None: # O(1)
            print("No hay paradas en la lista.") # O(1)
            return
        print("Listado de paradas:") # O(1)
        while control != None: # O(n)
            print(f"La parada {control.data}") # O(1)
            control = control.siguiente # O(1)
    
    def agregar(self, dato): 
        nuevo_nodo = Nodo(dato) # O(1)
        nuevo_nodo.siguiente = self.cabeza # O(1)
        self.cabeza = nuevo_nodo # O(1)
    
    def busqueda(self, dato):
        control = self.cabeza # O(1)
        contador = 1  # O(1)
        while control.data == dato or control == None: # O(n)
             contador += 1 # O(1)
             control = control.siguiente # O(1)
        if(control == None): # O(1)
            print("La parada no se encunetra en la lista") # O(1)
        else:
            print(f"La parada se encuentra en la posicion {contador}") # O(1)
    
    def eliminarParada(self):
        if self.cabeza != None: # O(1)
            print(f"Eliminando la parada: {self.cabeza.data}") # O(1)
            self.cabeza = self.cabeza.siguiente # O(1)
        else:
            print("No hay paradas para eliminar") # O(1)

# Ejemplo de uso
lista_paradas = ListaParadas() 
lista_paradas.agregar("Centro Comercial Cacique")
lista_paradas.agregar("Avenida Principal")
lista_paradas.agregar("Plaza Satelite")
lista_paradas.agregar("Universidad Industrial de Santander")
lista_paradas.agregar("Estación Metrolinea")

lista_paradas.imprimir()
lista_paradas.contar()
lista_paradas.busqueda("Plaza Satelite")
lista_paradas.eliminarParada()
lista_paradas.imprimir()
