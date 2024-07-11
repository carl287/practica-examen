
from os import system #el import es fundamental para importar los archivos (en este caso, queremos importar el archivo "calificaciones.csv")
import csv #aqui esto ayuda a importar el archivo "import csv"

def obtener_fichero_asistencia(): #aqui obtendremos la informacion del archivo
    lista=[] #aqui se crea un diccionario 
    with open("calificaciones.csv", "r", newline="") as archivo: #abrimos el directorio, pero solo para leerlo
        lector_csv= csv.reader(archivo, delimiter=";") #con esto se leera el archivo
        pos=0 #el lector estara en la posicion inicial del archivo
        for linea in lector_csv: #con este ciclo leeremos el archivo
            if pos!=0:
                curso=linea[0]
                rut=linea[1]
                nombre=linea[2]+ " "+linea[3]+ " "+linea[4]
                asistencia_actual=round(int(linea[5])/(int(linea[5])+int(linea[6])+int(linea[7]))*100,1)#esa es la formula para el porcentaje de asistencia
                lista.append({
                    "curso":curso,
                    "rut":rut,
                    "nombre":nombre,
                    "asistencia_actual":asistencia_actual,
                }) #ordenamos las variables en un diccionario
            else:
                pos=1
    return lista

