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
    def __init__(self, titulo, artista, id_departamento, tipo, anio_creacion, imagen_obra):
        self.titulo = titulo
        self.artista = artista
        self.id_departamento = id_departamento
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_obra = imagen_obra