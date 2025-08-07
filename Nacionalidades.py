class Nacionalidad:
    """
    Crea las nacionalidades de los autores.
    
    Atributos:
        nacionalidad
    """
    def __init__(self, nacionalidad):
        self.nacionalidad = nacionalidad
        
    def show(self):
        print(f"{self.nacionalidad}")
