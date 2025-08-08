class Obra:
    
    def __init__(self, titulo, artista, nacionalidad_artista, nacimiento_artista, muerte_artista, tipo, anio_creacion, imagen_obra):
        """
        Información de las obras.
        
        Args:
            titulo (str): Título de la obra.
            artista (str): Nombre del artista. 
            nacionalidad_artista (str): Nacionalidad del artista 
            nacimiento_artista : Año de nacimiento del artista.
            muerte_artista : Año de muerte del artista.
            tipo (str): Tipo de obra.
            anio_creacion : Año de la obra.
            imagen_obra (str): URL de la imagen de la obra.        
        """
        self.titulo = titulo
        self.artista = artista
        self.nacionalidad_artista = nacionalidad_artista
        self.nacimiento_artista = nacimiento_artista
        self.muerte_artista= muerte_artista
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_obra = imagen_obra
        
    def show(self):
        """
        Mostrar los datos de las obras.
        """
        print(f"""Título: {self.titulo}
Nombre del artista: {self.artista}
Nacionalidad del artista: {self.nacionalidad_artista}
Fecha de nacimiento del artista: {self.nacimiento_artista}
Fecha de muerte del artista: {self.muerte_artista}
Tipo de obra: {self.tipo}
Año de creación: {self.anio_creacion}
Imagen de la obra: {self.imagen_obra}""")
