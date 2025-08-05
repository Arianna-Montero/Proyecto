from Departamento import Departamento
from Obra import Obra
from Autor import Autor
class Museo:
    def __init__(self, objects_datos, object_datos, deparments_datos, search_datos_departamentos, search_datos_localitation):
        self.objects_datos=objects_datos
        self.object_datos=object_datos
        self.deparments_datos=deparments_datos
        self.search_departamentos=search_datos_departamentos
        self.search_lacalitation= search_datos_localitation

    
    def start(self):
        
        while True:
            busqueda=input("""Bienvenido al sistema de Catálogo de la colección de arte del Museo metropolitano de Art.
Elija una opción de búqueda de obras:
1- Ver lista de obras por Departamento
2- Ver lista de obras por Nacionalidad del autor
3- Ver lista de obras por nombre del autor
4- Salir

---->""")
            if busqueda == "1":
                #print(self.deparments_datos)

    def crear_objetos(self):
        
        departamentos_dic = self.deparments_datos
        obras_dic = self.object_datos

        self.departamentos = []
        self.autores = []
        self.obras= []

        for departamento in departamentos_dic:
            self.departamentos.append(Departamento(departamento["displayName"], departamento["departmentId"]))
        
        for autor in obras_dic:
            self.autores.append(Autor(autor["artistDisplayName"], autor["artistNationality"], autor["artistBeginDate"], autor["artistEndDate"]))

        for obra in obras_dic:
            departamento_encontrado = None
            for departamento in self.departamentos:
                if departamento.id == obra["id_departamento"]:
                    departamento_encontrado == departamento
        
        self.obras.append(Obra(obra["title"], obra["artistDisplayName"], departamento_encontrado, obra["objectName"], obra["objectBeginDate"], obra["primaryImage"]))
