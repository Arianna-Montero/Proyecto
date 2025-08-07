from Museo import Museo
from bd import deparments_datos, objects_datos, nacionalidades

def main():
    museo=Museo(deparments_datos, objects_datos, nacionalidades)
    museo.start()
main()
