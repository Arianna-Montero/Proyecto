class Museo:
    def __init__(self, objects_datos, object_datos, deparments_datos, search_datos):
        self.objects_datos=objects_datos
        self.object_datos=object_datos
        self.deparments_datos=deparments_datos
        self.search_datos=search_datos
    
    def start(self):
        
        while True:
            busqueda=input("""Bienvenido al sistema de Catálogo de la colección de arte del Museo metropolitano de Art.
Elija una opción de búqueda de obras:
1- Ver lista de obras por Departamento
2- Ver lista de obras por Nacionalidad del autor
3- Ver lista de obras por nombre del autor
4- Salir

---->""")