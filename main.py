

def obtener_csv_como_lista_de_diccionarios(calificaciones):
    separador = ","
    with open(calificaciones, encoding="utf-8") as archivo:
        next(archivo)  
        alumnos = []

        for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)
            Nombre = columnas[0]
            Apellidos = columnas[0]
            Nombre = columnas[1]
            Asistencia = columnas[2]
            Parcial1 = columnas[3]
            Parcial2 = columnas[4]
            Practicas = columnas[5]
            
            alumnos.append({
                "Apellidos": Apellidos,
                "Nombre": Nombre,
                "Asistencia": Asistencia,
                "Parcial1": Parcial1,
                "Parcial2": Parcial2,
                "Practicas": Practicas,
            })
        return alumnos

obtener_csv_como_lista_de_diccionarios("calificaciones.csv")


