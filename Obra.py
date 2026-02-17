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
    def __init__(self, titulo, artista, nacionalidad, fecha_nacimiento, fecha_muerte, tipo, anio_creacion, imagen_obra):
        self.titulo = titulo
        self.artista = artista
        self.nacionalidad = nacionalidad          
        self.fecha_nacimiento = fecha_nacimiento  
        self.fecha_muerte = fecha_muerte          
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_obra = imagen_obra

    def show(self):
        print(f"""Título: {self.titulo}
Nombre del artista: {self.artista}
Nacionalidad: {self.nacionalidad}
Fecha de nacimiento: {self.fecha_nacimiento}
Fecha de muerte: {self.fecha_muerte}
Tipo de obra: {self.tipo}
Año de creación: {self.anio_creacion}
Imagen de la obra: {self.imagen_obra}""")
        
