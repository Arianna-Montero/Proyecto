from Museo import Museo
from bd import objects_datos, deparments_datos, nacionalidades

def main():
    museo=Museo(objects_datos, deparments_datos, nacionalidades)
    museo.start()
main()
