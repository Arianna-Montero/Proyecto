class Departamento:

    def __init__(self, nombre_departamento, id):
        self.nombre_departamento = nombre_departamento
        self.id = id
    def show (self):
        print (f"""Nombre del departamento: {self.nombre_departamento}.
ID: {self.id}""")
