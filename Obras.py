class Obras:
    def __init__(self, id, titulo, autor):
        self.id= id
        self.tiutlo= titulo
        self.autor= autor

    def show(self):
        print(f"""ID de la obras: {self.id}
Titulo: {self.tiutlo}
Autor: {self.autor}""")
