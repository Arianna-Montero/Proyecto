from Departamento import Departamento
from Obra import Obra
from Autor import Autor
import requests

class Museo:
    def __init__(self, objects_datos, object_datos, deparments_datos):
    #, search_datos_departamentos, search_datos_localitation
        self.objects_datos=objects_datos
        self.object_datos=object_datos
        self.deparments_datos=deparments_datos
        #self.search_departamentos=search_datos_departamentos
        #self.search_lacalitation= search_datos_localitation

    
    def start(self):
        self.crear_objetos()
        self.crear_obejtos2()
        
        while True:
            print()
            busqueda=input("""Bienvenido al sistema de Catálogo de la colección de arte del Museo metropolitano de Art.
Elija una opción de búqueda de obras:
1- Ver lista de obras por Departamento
2- Ver lista de obras por Nacionalidad del autor
3- Ver lista de obras por nombre del autor
4- Salir

---->""")
            print()
           
            if busqueda == "1":
                for departamento in self.departamentos:
                    departamento.show()
                    print()
            
                self.buscar_obra_departamentoID()

                self.mostrar_obra()
                    
            elif busqueda== "2":
                
                for nacionalidad in self.nacionalidades:
                    print(nacionalidad)
                    
                self.buscar_obra_nacionalidad()
                
                self.mostrar_obra()

            elif busqueda == "3":
                for autor in self.autores:
                    autor.show()
                    print()
                self.buscar_obra_autor()
                self.mostrar_obra()

            elif busqueda== "4":
                break
            else:
                print("No válido, ingrese un número")
                print()
    

    
    def mostrar_obra(self):
        obraID = int(input("Ingrese el id de la obra que desea ver: "))
        print()
        object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obraID}") 
        obra= object_list.json()
    
        departamento_encontrado= None
        for departamento in self.departamentos:
            if departamento.id == obra.get("departmentId"):
                departamento_encontrado == departamento
        self.obras.append(Obra(obra.get("title"), obra.get("artistDisplayName"), departamento_encontrado, obra.get("objectName"), obra.get("objectBeginDate"), obra.get("primaryImage")))
        for obra in self.obras:
            obra.show()
            print()

        



    def buscar_obra_autor(self):
        nombre_autor = input("Escriba el nombre del autor: ")
        search_obras_autor = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}")
        search_autor = search_obras_autor.json() 
        print(search_autor)
         
                
    def buscar_obra_nacionalidad(self):
            nacionalidad= input("Ingrese la nacionalidad del autor: ")
            search_obras_localidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}")
            search_localidad = search_obras_localidad.json() 
            print(search_localidad)

    def buscar_obra_departamentoID(self):
        obras_departamento = int(input("Escriba el ID del departamento para ver las obras: "))
        print()
        search_obras_departamento = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={obras_departamento}&q=cat") 
        search_departamento = search_obras_departamento.json()
        print(search_departamento)
        print()
    
    def crear_objetos(self):
        
        departamentos_dic = self.deparments_datos.json()
        #obras_rec = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects", timeout=40)
        #obras_dic= obras_rec.json()

        self.departamentos = []
        self.autores = []
        self.obras= []

        for departamento in departamentos_dic["departments"]:
            self.departamentos.append(Departamento(departamento["displayName"], departamento["departmentId"]))
        
        
        #for objectID in obras_dic["objectIDs"]:
            #try:
                #object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}", timeout=20) 
                #obras= object_list.json()
        #self.autores.append(Autor(obra["artistDisplayName"], obra["artistNationality"], obra["artistBeginDate"], obra["artistEndDate"]))
            #except requests.exceptions.RequestException as err:
                #pass
                #print(f"Error al procesar el objeto {objectID}: {err}")


        #for objectID in obras_dic["objectIDs"]:
            #departamento_encontrado = None
            #object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}") 
            #obras= object_list.json()
            #for departamento in self.departamentos:
               #if departamento.id == obras.get("departmentId"):
                  #departamento_encontrado == departamento
        
        #self.obras.append(Obra(obras["title"], obras["artistDisplayName"], departamento_encontrado, obras["objectName"], obras["objectBeginDate"], obras["primaryImage"]))
        #Ari hay que crear clases u objetos de los "search" porque todos los diccionarios deben ser objetos y ver como hacemos una clase de autores que sirva pq ya me rendí.
    
    def crear_obejtos2(self):
        nacionalidades_dic = self.objects_datos.json()
        todas_ids = nacionalidades_dic["objectIDs"][:3]
            
        self.nacionalidades = []
            
        for nacionalidad in todas_ids:
            mucho_dato = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{nacionalidad}")
            datos = mucho_dato.json()
                
            self.nacionalidades.append(datos["artistNationality"])

