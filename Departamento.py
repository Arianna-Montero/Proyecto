class Departamento:

    def __init__(self, nombre_departamento, id):
        """
        Nombre de departamento.
        
        Args:
            nombre_departamento (str): Nombre del departamento.
            id : ID del departamento.
        """
        self.nombre_departamento = nombre_departamento
        self.id = id
        
    def show (self):
        """
        Mostrar nombre del departamento.
        """
        print (f"""Nombre del departamento: {self.nombre_departamento}.
ID: {self.id}""")
