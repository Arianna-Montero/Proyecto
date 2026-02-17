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
    def show(self):
        print(f"""Artista: {self.nombre_artista}
Nacionalidad: {self.nacionalidad_artista}
Fecha de nacimiento: {self.fecha_nacimiento}
Fecha de muerte: {self.fecha_muerte}""")
