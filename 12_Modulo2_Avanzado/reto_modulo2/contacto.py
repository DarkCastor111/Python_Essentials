class Contacto:

    def __init__(self, nm, tlf, email):
        self.validar_campo(nm)
        self.validar_campo(tlf)
        self.validar_campo(email)
        self.validar_email(email)
        self.nombre = nm
        self.telefono = tlf
        self.correo = email


    def __str__(self):
        return (f'Contacto: {self.nombre} - tlf:{self.telefono} - correo:{self.correo}')

    def to_string_archivo(self):
        return (f'{self.nombre},{self.telefono},{self.correo}\n')
    
    def validar_email(self, email):
        if len(email) < 6 or not "@" in email or "." not in email.split("@")[-1]:
            raise ValueError("Email inválido. Debe contener '@' y un dominio.")

    def validar_campo(self, campo):
        if len(campo) == 0 or "," in campo:
            raise ValueError("Un campo no puede ser vacío y no puede tener comas")

