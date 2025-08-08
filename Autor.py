class Autor:
  
    def __init__(self, nombre_artista):
        """
        Nombre de autor.
        
        Args:
            nombre_artista (str): Nombre del autor.
        """
        self.nombre_artista = nombre_artista
        
    def show(self):
        """
        Mostrar nombre del autor.
        """
        print(f"Artista: {self.nombre_artista}")
        
