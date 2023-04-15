

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



def agregar_nota_final(calificaciones):
    for alumno in calificaciones:
        parcial1=float(alumno['Parcial1'])
        parcial2=float(alumno['Parcial2'])
        practicas=float(alumno['Practicas'])
        
        nota_parciales= parcial1*0.3 + parcial2*0.3
        nota_practicas=practicas*0.4
        nota_final=nota_parciales + nota_practicas
        alumno["Nota final"]= nota_final
        return calificaciones 
 
def listas_aprobados_suspensos(calificaciones):
    suspensos=[]
    aprobados=[]
    for alumno in calificaciones:
        if alumno["Nota final"]<=5 or alumno["Asistencia"]<75:
            suspensos.append(alumno)
        else:
            aprobados.append(alumno)
     
    return (aprobados,suspensos)
         