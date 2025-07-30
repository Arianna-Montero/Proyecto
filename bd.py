import requests
"""
Acceder a los datos de las obras del museo
"""

objects = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
object = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/[objectID]")
deparments = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
search = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search")

objects_datos = objects.json()
object_datos = object.json()
deparments_datos = deparments.json()
search_datos = search.json()
