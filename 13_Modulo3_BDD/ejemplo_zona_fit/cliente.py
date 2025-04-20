class Cliente:
    def __init__(self, p_id=None, p_nombre=None, p_apellido=None, p_membresia=None):
        self.id = p_id
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.membresia = p_membresia

    def __str__(self):
        return f'Cliente: #{self.id} - {self.nombre} {self.apellido} - {self.membresia}'
