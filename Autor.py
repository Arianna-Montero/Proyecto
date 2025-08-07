class Autor:
    """
    Crear autores de las obras
    
    Atributos:
        nombre_artista (str)       
    """    
    def __init__(self, nombre_artista):
        self.nombre_artista = nombre_artista
    def show(self):
        print(f"""Artista: {self.nombre_artista}""")

