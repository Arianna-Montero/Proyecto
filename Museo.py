from Departamento import Departamento
from Obra import Obra
from Autor import Autor
from Obras import Obras
from Nacionalidades import Nacionalidad

import requests

from PIL import Image
from Imagen import guardar_imagen_desde_url

class Museo:
    def __init__(self, deparments_datos, objects_datos, nacionalidades):
        self.objects_datos=objects_datos
        self.deparments_datos=deparments_datos
        self.nacionalidades= nacionalidades
        
        self.departamentos = []
        self.obras = []
        self.autores = []

    def start(self):
        self.crear_objetos()
                
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
                
                self.obras = []
                
                for departamento in self.departamentos:
                    departamento.show()
                    print()
            
                self.buscar_departamentoID()

                self.mostrar_obra()
                                    
            elif busqueda== "2":
                
                self.obras = []
                
                self.mostrar_nacionalidades()
                self.buscar_obra_nacionalidad()
                self.mostrar_obra()

            elif busqueda == "3":
                
                self.obras = []
                
                lista_autores = self.autores_aleatorio()
                                
                print("Autores: ")
                
                for autor_nombre in lista_autores:
                    print(f"- {autor_nombre}")

                for autor in self.autores:
                    autor.show()
                    print()
                                      
                self.buscar_obra_autor()
                
                self.mostrar_obra()

            elif busqueda== "4":
                print("Gracias por visitarnos")
                print()
                break
            
            else:
                print("No válido, ingrese un número")
                print()
           
    def crear_objetos(self):
        
        departamentos_dic = self.deparments_datos
        nacionalidaddes_dic = self.nacionalidades
        
        #self.departamentos = []
        #self.obras= []
        self.nacionalidades= []
        #self.autores = []
        
        if "departments" in departamentos_dic:
            
            for departamento in departamentos_dic:
                self.departamentos.append(Departamento(departamento["displayName"], departamento["departmentId"]))
                
        else:
            print("Error: No se pudieron cargar los datos de los departamentos. Verifica la conexión a la API o el formato de los datos.")
            
        
        for nacionalidad in nacionalidaddes_dic:
            self.nacionalidades.append(Nacionalidad(nacionalidad))
        
        #autores_nombres = self.autores_abecedario()
        #for autor in autores_nombres:
        #    self.autores.append(Autor(autor, None, None, None))
    
    def mostrar_obra(self):
        
        obraID = int(input("Ingrese el id de la obra que desea ver: "))
        print()
        
        try:
            
            object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obraID}", timeout= 20) 
            obra_detalles= object_list.json()
            
            self.obras.append(Obra(obra_detalles.get("title"), obra_detalles.get("artistDisplayName"), obra_detalles.get("artistNationality"), obra_detalles.get("artistBeginDate"), obra_detalles.get("artistEndDate"), obra_detalles.get("objectName"), obra_detalles.get("objectDate"), obra_detalles.get("primaryImage")))
            
            for obra in self.obras:
                obra.show()
                print()   
                   
            id = input("""¿Mostrar imagen?
-> Si
-> No                           
""")
            print(id)
            
            if id == "Si":
                
                if obra_detalles.get("primaryImage"):
                    nombre_archivo = guardar_imagen_desde_url(obra_detalles["primaryImage"], f"obra_{obraID}")
                        
                    img = Image.open(nombre_archivo)
                    img.show()
                
                else:
                    pass
                
        except requests.exceptions.RequestException as e:
            print("ID no encontrado")                       
                                        
    def buscar_departamentoID(self):
        
        obras_departamentos = int(input("Escriba el ID del departamento para ver las obras: "))
        print()
        
        try:
            
            obras_departamento = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={obras_departamentos}&q=cat") 
            buscar_departamento = obras_departamento.json()
            obras_ids = buscar_departamento["objectIDs"]
            
            for id in obras_ids[:3]:
                
                try:
                    
                    obras_encontradas = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20)         
                    mostrar_obra = obras_encontradas.json()
                    
                    self.obras.append(Obras(mostrar_obra.get("objectID"), mostrar_obra.get("title"), mostrar_obra.get("artistDisplayName")))
                    
                    for obra in self.obras:
                        obra.show()
                        print()
                        
                    #print(f"Id de la obra: {mostrar_obra["objectID"]}, Título: {mostrar_obra["title"]}, Nombre del autor: {mostrar_obra["artistAlphaSort"]}")
                
                except requests.exceptions.RequestException as e:
                    break
        
        except requests.exceptions.RequestException as e:
            
            print("Departamento no encontrado")
            return
          
    def buscar_obra_nacionalidad(self):
        nacionalidad = input("Ingrese la nacionalidad de las obras que desea ver: ")
        print(nacionalidad)
        
        try:
            
            buscar_nacionalidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}")
            
            obra_nacionalidad = buscar_nacionalidad.json()
            todas_ids = obra_nacionalidad["objectIDs"]
            
            #self.nacionalidades = []
                
            for id in todas_ids[:3]:
                
                try:
                    
                    mucho_dato = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}")
                    datos = mucho_dato.json()
                    
                    #print(f"Id de la obra: {datos["objectID"]}, Título: {datos["title"]}, Nombre del autor: {datos["artistAlphaSort"]}")

                    self.obras.append(Obras(datos.get("objectID"), datos.get("title"), datos.get("artistDisplayName")))
                    
                    for obra in self.obras:
                        obra.show()
                        print()
                        
                except requests.exceptions.RequestException as e:
                    print("No se pudo encontrar las obras")
                    break
                    
        except requests.exceptions.RequestException as e:
                    print("No se pudo encontrar la nacionalidad")
                    return
                
    def mostrar_nacionalidades(self):
        for nacionalidad in self.nacionalidades:
            nacionalidad.show()
                    
    def autores_aleatorio(self):
        """
        Obtener autores aleatoriamente.
        """
        buscar_aleatorio = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=*")
        id_aleatorio = buscar_aleatorio.json()
        ids_obras = id_aleatorio.get("objectIDs")[:25]
        
        autores = []
            
        for id_obra in ids_obras:
                
            buscar_obra = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}")
            obra = buscar_obra.json()
            
            if "artistDisplayName" in obra and obra["artistDisplayName"]:

                buscar_nombre = obra.get("artistDisplayName")
                
                if buscar_nombre not in autores:
                    autores.append(buscar_nombre)
            
        return autores
              
    def buscar_obra_autor(self):
        nombre_autor = input("Escriba el nombre del autor: ")
        
        try:
        
            search_obras_autor = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}")
            search_autor = search_obras_autor.json()
            autor_ids = search_autor["objectIDs"]
            
            for id in autor_ids[:3]:
                
                try:
                    
                    object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20) 
                    obra= object_list.json()
                    
                    self.obras.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
                    
                    for obra in self.obras:
                        obra.show()
                        print()
                    
                except requests.exceptions.RequestException as e:
                    break
    
        except requests.exceptions.RequestException as e:
                print("No se pudo encontrar al autor")
                return
        
        #self.obras.append(Obras(obra["objectIDs"]))
        #print(f"Id de la obra: {mostrar_obra["objectID"]}, Título: {mostrar_obra["title"]}, Nombre del autor: {mostrar_obra["artistAlphaSort"]}")
    
        #for id in search_departamento["objectIDs"]:
        #        try:
        #            object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20) 
        #            obra= object_list.json()
        #            self.obras.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
        #            for obra in self.obras:
        #                obra.show()
        #                print()
                
        #        except requests.exceptions.RequestException as e:
        #            break

