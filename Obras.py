class Obras:
    def __init__(self, id, titulo, autor):
        """
        Obras.
        
        Args:
            id (int): ID de la obra.
            titulo (str): Título de la obra.
            autor (str): Nombre del autor.
        """
        self.id= id
        self.tiutlo= titulo
        self.autor= autor

    def show(self):
        """
        Mostrar obras.
        """
        print(f"""ID de la obras: {self.id}
Titulo: {self.tiutlo}
Autor: {self.autor}""")
        
