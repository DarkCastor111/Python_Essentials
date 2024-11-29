import pickle
from pathlib import Path

#Empty dictionary
d = dict()

file_name = input("Nombre del archivo con los datos: ")

path = Path(file_name)
if path.is_file():
    # Open file in reading mode
    input_file = open(file_name, 'rb')
    d = pickle.load(input_file)
    # Close file
    input_file.close()
else:
    print("El archivo no existe, creamos un nuevo")

# Check for values or add new ones
document_number = input("Documento de identidad: ")

if document_number in d:
    print("La edad de " + document_number + " es " + str(d[document_number]))
else:
    age = input("Document no existente. Introduce edad: ")
    if age.isnumeric():
        num = int(age)
        d[document_number] = num
        print("Añadido al diccionario")

# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()

