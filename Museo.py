from Departamento import Departamento
from Obra import Obra
from Autor import Autor
from Obras import Obras
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
                
                nacionalidades = ["Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Anguillan", "Argentine", "Armenian", "Australian", "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese", "Bermudian", "Bhutanese", "Bolivian", "Botswanan", "Brazilian", "British", "British Virgin Islander", "Bruneian", "Bulgarian", "Burkinan", "Burmese", "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", "Cayman Islander", "Central African", "Chadian", "Chilean", "Chinese", "Citizen of Antigua and Barbuda", "Citizen of Bosnia and Herzegovina", "Citizen of Guinea-Bissau", "Citizen of Kiribati", "Citizen of Seychelles", "Citizen of the Dominican Republic", "Citizen of Vanuatu", "Colombian", "Comoran", "Congolese (Congo)", "Congolese (DRC)", "Cook Islander", "Costa Rican", "Croatian", "Cuban", "Cymraes", "Cymro", "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican", "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirati", "English", "Equatorial Guinean", "Eritrean", "Estonian", "Ethiopian", "Faroese", "Fijian", "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German", "Ghanaian", "Gibraltarian", "Greek", "Greenlandic", "Grenadian", "Guamanian", "Guatemalan", "Guinean", "Guyanese", "Haitian", "Honduran", "Hong Konger", "Hungarian", "Icelandic", "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakh", "Kenyan", "Kittitian", "Kosovan", "Kuwaiti", "Kyrgyz", "Lao", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtenstein citizen", "Lithuanian", "Luxembourger", "Macanese", "Macedonian", "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese", "Marshallese", "Martiniquais", "Mauritanian", "Mauritian", "Mexican", "Micronesian", "Moldovan", "Monegasque", "Mongolian", "Montenegrin", "Montserratian", "Moroccan", "Mosotho", "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerian", "Nigerien", "Niuean", "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Pitcairn Islander", "Polish", "Portuguese", "Prydeinig", "Puerto Rican", "Qatari", "Romanian", "Russian", "Rwandan", "Salvadorean", "Sammarinese", "Samoan", "Sao Tomean", "Saudi Arabian", "Scottish", "Senegalese", "Serbian", "Sierra Leonean", "Singaporean", "Slovak", "Slovenian", "Solomon Islander", "Somali", "South African", "South Korean", "South Sudanese", "Spanish", "Sri Lankan", "St Helenian", "St Lucian", "Stateless", "Sudanese", "Surinamese", "Swazi", "Swedish", "Swiss", "Syrian", "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian", "Tristanian", "Tunisian", "Turkish", "Turkmen", "Turks and Caicos Islander", "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbek", "Vatican citizen", "Venezuelan", "Vietnamese", "Vincentian", "Wallisian", "Welsh", "Yemeni", "Zambian", "Zimbabwean"]
                
                for nacion in nacionalidades:
                    print(nacion)
                               
                #for nacionalidad in self.nacionalidades:
                    #print(nacionalidad)
                    
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
        object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obraID}", timeout= 30) 
        
        #obra= object_list.json() #<-código ari
        #departamento_encontrado= None
        #for departamento in self.departamentos:
        #    if departamento.id == obra.get("departmentId"):
        #        departamento_encontrado == departamento
        #self.obras.append(Obra(obra.get("title"), obra.get("artistDisplayName"), departamento_encontrado, obra.get("objectName"), obra.get("objectBeginDate"), obra.get("primaryImage")))
        #for obra in self.obras:
        #    obra.show()
        #    print() #tooodo código ari
        
        obra_m= object_list.json()
        self.obras.append(Obra(obra_m.get("title"), obra_m.get("artistDisplayName"), obra_m.get("artistNationality"), obra_m.get("artistBeginDate"), obra_m.get("artistEndDate"), obra_m.get("objectName"), obra_m.get("objectDate"), obra_m.get("primaryImage")))
        for obra in self.obras:
            obra.show()
            print()
                
    def buscar_obra_departamentoID(self):
        obras_departamento = int(input("Escriba el ID del departamento para ver las obras: "))
        print()
        
        search_obras_departamento = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={obras_departamento}&q=cat") 
        search_departamento = search_obras_departamento.json()
        
        obras_ids = search_departamento["objectIDs"]
        for id in obras_ids[:30]:
            obras_encontradas = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20)         
            mostrar_obra = obras_encontradas.json()
            
            print(f"Id de la obra: {mostrar_obra["objectID"]}, Título: {mostrar_obra["title"]}, Nombre del autor: {mostrar_obra["artistAlphaSort"]}")
            
            #self.mostrar_obra.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
            #for obra in self.obras:
                #obra.show()
                #print()
          
    def buscar_obra_nacionalidad(self):
        
        nacionalidad = str(input("Ingrese la nacionalidad de las obras que desea ver: "))
        print(nacionalidad)
        
        search_nacionalidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}")
        
        obra_nacionalidad = search_nacionalidad.json()
        todas_ids = obra_nacionalidad["objectIDs"]
        
        self.nacionalidades = []
               
        for id in todas_ids:
            
            mucho_dato = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}")
            datos = mucho_dato.json()
            
            print(f"Id de la obra: {datos["objectID"]}, Título: {datos["title"]}, Nombre del autor: {datos["artistAlphaSort"]}")
            
            #self.nacionalidades.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))     
            #for obra in self.obras:
                #obra.show()
                #print()
                   
    
        
    def buscar_obra_autor(self):
        nombre_autor = input("Escriba el nombre del autor: ")
        search_obras_autor = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}")
        search_autor = search_obras_autor.json() 
        #print(search_autor) #<-código ari
        
        for id in search_autor["objectIDs"]:
            try:
                object_list = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}", timeout=20) 
                obra= object_list.json()
                self.obras.append(Obras(obra.get("objectID"), obra.get("title"), obra.get("artistDisplayName")))
                for obra in self.obras:
                    obra.show()
                    print()
                
            except requests.exceptions.RequestException as e:
                break
   
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
        
