class Obra:
    """
    Crear obras del museo
    
    Atributos:
        titulo (str)
        artista 
        id_departamento 
        tipo 
        anio_creacion 
        imagen_obra (str)        
    """
    def __init__(self, titulo, artista, nacionalidad_artista, fecha_nacimeinto_art, fecha_muerte_art, tipo, anio_creacion, imagen_obra):
        self.titulo = titulo
        self.artista = artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_na_art = fecha_nacimeinto_art
        self.fecha_mue_art= fecha_muerte_art
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_obra = imagen_obra

    def show(self):
        print(f"""Título: {self.titulo}
Nombre del artista: {self.artista}
Nacionalidad del artista: {self.nacionalidad_artista}
Fecha de naciomiento del artista: {self.fecha_na_art}
Fecha de muerte del artista: {self.fecha_mue_art}
Tipo de obra: {self.tipo}
Año de creación: {self.anio_creacion}
Imagen de la obra: {self.imagen_obra}""")

