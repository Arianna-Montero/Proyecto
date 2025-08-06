import Museo
import requests
"""
Acceder a los datos de las obras del museo
"""

objects = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects") #200
deparments = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments") #200

#search_obras_departamento = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=[departmentId]&q=cat") 
search_obras_localidad = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?geoLocation=[geoLocation]&q=flowers") 
search_obras_departamento = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=[departmentId]&q=cat") 

#object = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects") #400

#objects_datos = objects.json()
#object_datos = object.json()
deparments_datos= deparments.json()
#search_localidad = search_obras_localidad.json()
#print(f"Código de estado: {object.status_code}")
#print(f"Texto de la respuesta:\n{objects.text}")

