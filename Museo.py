from Departamento import Departamento
from Obra import Obra
from Autor import Autor
from Obras import Obras

import requests

from PIL import Image
from Imagen import guardar_imagen_desde_url

class Museo:
    def __init__(self, objects_datos, deparments_datos, nacionalities):
        self.objects_datos=objects_datos
        self.deparments_datos=deparments_datos
        self.nacionalities= nacionalities

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
                for departamento in self.departamentos:
                    departamento.show()
                    print()
            
                self.buscar_obra_departamentoID()

                self.mostrar_obra()
                                    
            elif busqueda== "2":
                
                self.mostrar_nacionalidades()
                self.buscar_obra_nacionalidad()
                self.mostrar_obra()

            elif busqueda == "3":
                
                print("Autores: ")
                
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
    
    def crear_objetos_departamento(self):
        
        departamentos_dic = self.deparments_datos.json()
        nacionalidaddes_dic = self.nacionalities
        self.departamentos = []
        self.obras= []
        self.nacionalidades= []
        self.autores = []
        
        for nacionalidad in nacionalidaddes_dic:
            self.nacionalidades.append(Nacionalidad(nacionalidad))
        
        for departamento in departamentos_dic["departments"]:
            self.departamentos.append(Departamento(departamento["displayName"], departamento["departmentId"]))
        
        autores_nombres = self.autores_abecedario()
        for autor in autores_nombres:
            self.autores.append(Autor(autor, None, None, None))
        
        
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
        #deberiamos borrar todo esto
    
def mostrar_obra(self):
    
        obraID = int(input("Ingrese el id de la obra que desea ver: "))
        print()
        try:
            object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obraID}", timeout= 20) 
            obra_m= object_list.json()
            self.obras.append(Obra(obra_m.get("title"), obra_m.get("artistDisplayName"), obra_m.get("artistNationality"), obra_m.get("artistBeginDate"), obra_m.get("artistEndDate"), obra_m.get("objectName"), obra_m.get("objectDate"), obra_m.get("primaryImage")))
            for obra in self.obras:
                obra.show()
                print()   
          
        except requests.exceptions.RequestException as e:
            print("ID no encontrado")
            pass
        
        id = input("""¿Mostrar imagen?
-> Si
-> No                           
""")
        print(id)
        
        if id == "Si":
             
            if obra_m.get("primaryImage"):
                nombre_archivo_destino = guardar_imagen_desde_url(obra_m["primaryImage"], f"obra_{obraID}")
                    
                img = Image.open(nombre_archivo_destino)
                img.show()                       
                                        
    def buscar_obra_departamentoID(self):
         obras_departamento = int(input("Escriba el ID del departamento para ver las obras: "))
        print()
        try:
            search_obras_departamento = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={obras_departamento}&q=cat") 
            search_departamento = search_obras_departamento.json()
            for id in search_departamento["objectIDs"]:
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
             pass
            #self.mostrar_obra.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
            #for obra in self.obras:
                #obra.show()
                #print()
          
    def buscar_obra_nacionalidad(self):
        
       nacionalidad= input("Ingrese la nacionalidad del autor: ")
            print()
            try: 
                search_obras_localidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}")
                search_localidad = search_obras_localidad.json() 
                for id in search_localidad["objectIDs"]:
                    try:
                        object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20) 
                        obra= object_list.json()
                        self.obras.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
                        for obra in self.obras:
                            obra.show()
                            print()
                    except requests.exceptions.RequestException as e:
                        print("No se pudo encontrar las obras")
                        break
            except requests.exceptions.RequestException as e:
                    print("No se puso encontrar la nacionalidad")
                    pass
            #self.nacionalidades.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))     
            #for obra in self.obras:
                #obra.show()
                #print()
    
def mostrar_nacionalidades(self):
        for nacionalidad in self.nacionalidades:
            nacionalidad.show()               
    
    def autores_abecedario(self):
        """
        Obtener autores alfabeticamente.
        """
        letras = "abcdefghijklmnopqrstuvwxyz"
        autores = []
        
        for letra in letras:
            
            buscar_letra = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={letra}")
            id_letra = buscar_letra.json()
            ids_obras = id_letra.get("objectIDs")[:1]
            
            for id_obra in ids_obras:
                
                buscar_obra = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}")
                obra = buscar_obra.json()
                
                buscar_nombre = obra.get("artistDisplayName")
                
                if buscar_nombre not in autores:
                    autores.append(buscar_nombre)
        
        return autores
            
            
    
        
    def buscar_obra_autor(self):
        nombre_autor = input("Escriba el nombre del autor: ")
        try: 
            search_obras_autor = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}", timeout=20)
            search_autor = search_obras_autor.json()  
            for id in search_autor["objectIDs"]:
                try:
                    object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20) 
                    obra= object_list.json()
                    self.obras.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
                    for obra in self.obras:
                        obra.show()
                        print()
        #print(search_autor) #<-código ari
                except requests.exceptions.RequestException as e:
                    break
        except requests.exceptions.RequestException as e:
                print("No se puso encontrar al autor")
                pass
   
          
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

