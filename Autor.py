class Autor:
    """
    Crear autores de las obras
    
    Atributos:
        nombre_artista (str)
        nacionalidad_artista (str) 
        fecha_nacimiento 
        fecha_muerte        
    """    
    def __init__(self, nombre_artista, nacionalidad_artista, fecha_nacimiento, fecha_muerte):
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte