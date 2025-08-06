from Museo import Museo
from bd import objects, object, deparments, search_obras_localidad, search_obras_departamento
def main():
    museo=Museo(objects, object, deparments) #search_obras_localidad, search_obras_departamento)
    museo.start()
main()

