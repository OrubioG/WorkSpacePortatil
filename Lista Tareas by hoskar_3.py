# Defino mi clase lista de tareas
class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    # Este metodo agrega una nueva tarea a la lista como pendiente
    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "estado": "Pendiente"})
        print("Tarea agregada exitosamente.")

    # Este metedo marco la tarea como completada según su posición en la lista
    def marcar_tarea_como_completada(self, indice):     
        try:
            self.tareas[indice]["estado"] = "Completada"
            print("Tarea marcada como completada.")
        except IndexError:
            print("Número de tarea inválido.")
    # Este metodo muestro todas las tareas con su estado
    def mostrar_tareas(self):
        # Si no contiene tareas
        if not self.tareas:
            print("No hay tareas para mostrar.")
            return
        # Recorro las tareas y muestro su estado
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea['tarea']} [{tarea['estado']}]")

    # Este metodo elimina una tarea según su posición en la lista
    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
            print("Tarea eliminada exitosamente.")
        except IndexError:
            print("Número de tarea inválido.")
    # Este metodo ejecuta el programa de gestión de tareas
    def ejecutar(self):
        while True:
            print("\n1. Agregar Tarea\n2. Marcar Tarea como Completada\n3. Mostrar Tareas\n4. Eliminar Tarea\n5. Salir")
            eleccion = input("¿Qué quieres hacer?: ")
            # Una vez tengo la opcion elegida del usuario, voy mirando que valor tiene para realizar la tarea
            if eleccion == "1":
                tarea = input("Introduce la descripción de la tarea: ")
                self.agregar_tarea(tarea)
            elif eleccion == "2":
                self.mostrar_tareas()
                numero_tarea = int(input("¿Qué número de tarea quieres marcar como completada?: ")) - 1
                self.marcar_tarea_como_completada(numero_tarea)
            elif eleccion == "3":
                self.mostrar_tareas()
            elif eleccion == "4":
                self.mostrar_tareas()
                numero_tarea = int(input("¿Qué número de tarea quieres eliminar?: ")) - 1
                self.eliminar_tarea(numero_tarea)
            elif eleccion == "5":
                print("Saliendo del programa.")
                break
            else:#Controlo que se ha elegido una opción correcta
                print("Has seleccionado una opción inválida. SELECCIONE UNA OPCIÓN DEL 1 AL 5") 
                
                
# Ejecuto el programa
lista_de_tareas = ListaDeTareas()
lista_de_tareas.ejecutar()