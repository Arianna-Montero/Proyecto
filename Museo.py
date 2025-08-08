from Departamento import Departamento
from Obra import Obra
from Obras import Obras
from Nacionalidades import Nacionalidad

import requests

from PIL import Image
from Imagen import guardar_imagen_desde_url

class Museo:
    def __init__(self, objects_datos, deparments_datos, nacionalidades):
        """
        Datos del museo.
        
        Args:
            objects_datos (dict): IDS de las obras.
            deparments_datos (dict): Datos de los departamentos.
            nacionalidades (list): Nacionalidades.
        """
        self.objects_datos=objects_datos
        self.deparments_datos=deparments_datos
        self.nacionalidades= nacionalidades

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
                
                self.mostrar_departamentos()
                self.buscar_departamentoID()
                self.mostrar_obra()
                                    
            elif busqueda== "2":
                
                self.mostrar_nacionalidades()
                self.buscar_obra_nacionalidad()
                self.mostrar_obra()

            elif busqueda == "3":
                
                self.mostrar_autores()                                     
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
        nacionalidaddes_dic = self.nacionalidades

        self.departamentos = []
        self.obras= []
        self.nacionalidades= []
        self.autores = []
        
        for departamento in self.deparments_datos["departments"]:
            self.departamentos.append(Departamento(departamento["displayName"], departamento["departmentId"]))
        
        for nacionalidad in nacionalidaddes_dic:
            self.nacionalidades.append(Nacionalidad(nacionalidad))
    
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
            print()
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
            
            for id in obras_ids:
                
                try:
                    
                    obras_encontradas = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20)         
                    mostrar_obra = obras_encontradas.json()
                    
                    self.obras.append(Obras(mostrar_obra.get("objectID"), mostrar_obra.get("title"), mostrar_obra.get("artistDisplayName")))
                    
                    for obra in self.obras:
                        obra.show()
                        print()
                        
                except requests.exceptions.RequestException as e:
                    break
        
        except requests.exceptions.RequestException as e:
            
            print("Departamento no encontrado")
            return
          
    def mostrar_departamentos(self):
        for departamento in self.departamentos:
            departamento.show()
            print()      
    
    def buscar_obra_nacionalidad(self):
        nacionalidad = input("Ingrese la nacionalidad de las obras que desea ver: ")
        print()
        
        try:
            
            buscar_nacionalidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}")
            
            obra_nacionalidad = buscar_nacionalidad.json()
            todas_ids = obra_nacionalidad["objectIDs"]
               
            for id in todas_ids[:3]:
                
                try:
                    
                    mucho_dato = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}")
                    datos = mucho_dato.json()

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
    
    def mostrar_autores(self):
        
        lista_autores = self.autores_aleatorio()                     
        print("Autores: ") 
                   
        for autor_nombre in lista_autores:
            print(f"{autor_nombre}")
                    
    def autores_aleatorio(self):
        
        buscar_aleatorio = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=*")
        id_aleatorio = buscar_aleatorio.json()
        ids_obras = id_aleatorio.get("objectIDs")
        
        autores = []
            
        try:    
            for id_obra in ids_obras:
                
                buscar_obra = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}")
                obra = buscar_obra.json()  
                           
                if "artistDisplayName" in obra and obra["artistDisplayName"]:
                    buscar_nombre = obra.get("artistDisplayName")
                    
                    if buscar_nombre not in autores:
                        autores.append(buscar_nombre)
                        
        except requests.exceptions.RequestException as e:     
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
