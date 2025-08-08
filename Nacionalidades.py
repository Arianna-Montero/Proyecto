class Nacionalidad:
    
    def __init__(self, nacionalidad):
        """
        Nacionalidades de los autores.
        
        Atributos:
            nacionalidad (str): Nombre de la nacionalidad.
        """
        self.nacionalidad = nacionalidad
        
    def show(self):
        """
        Mostrar las nacionalidades de los autores.
        """
        print(f"{self.nacionalidad}")
        
