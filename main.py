from Museo import Museo
from bd import objects_datos, object_datos, deparments_datos, search_datos
def main():
    Museo=Museo(objects_datos, object_datos, deparments_datos, search_datos)
    Museo.start()
main()
