

def obtener_csv_como_lista_de_diccionarios(calificaciones):
    separador = ";"
    with open(calificaciones, encoding="utf-8") as archivo:
        next(archivo)  
        alumnos = []

        for linea in archivo:
            linea = linea.rstrip("\n")  
            columnas = linea.split(separador)
            Apellidos = columnas[0]
            Nombre = columnas[1]
            Asistencia = columnas[3]
            Parcial1 = columnas[4]
            Parcial2 = columnas[5]
            Practicas = columnas[6]

            alumnos.append({
                "Apellidos": Apellidos,
                "Nombre": Nombre,
                "Asistencia": Asistencia,
                "Parcial1": Parcial1,
                "Parcial2": Parcial2,
                "Practicas": Practicas,
            })
            print(alumnos)
        return alumnos

obtener_csv_como_lista_de_diccionarios("calificaciones.csv")



