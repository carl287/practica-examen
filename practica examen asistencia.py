
from os import system #el import es fundamental para importar los archivos (en este caso, queremos importar el archivo "calificaciones.csv")
import csv #aqui esto ayuda a importar el archivo "import csv"

def obtener_fichero_asistencia(): #aqui obtendremos la informacion del archivo
    lista=[] #aqui se crea un diccionario 
    with open("asistencia_alumnos.csv", "r", newline="") as archivo: #abrimos el directorio, pero solo para leerlo
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


def menu_principal(): #aqui crearemos el menu
    opciones= {
        "1": ("consultar asistencia actual del alumno", consultar_asistencia_rut),
        "2": ("visualizar alumnos de asistencia actual < 70%", visualiza_asistencia_70),
        "3": ("visualizar numero de alumnos con asistencia actual < 70% de un curso", visualiza_asistencia_curso),
        "4": ("generar archivos alumnos con una asistencia actual < 70% de un curso", generar_asistencia_curso),
        "5": ("salir", salir)
    }  #como se puede ver, generamos las opciones con un diccionario para que cuando generemos la entrada de elegir opcion, lo busque en la funcion con palabra clave

    generar_menu(opciones,"5") #este servira cuando generemos la funcion de elegir opcion, teniendo 5 palabras clave

def generar_menu(opciones, opcion_salida): #aqui generaremos las palbras clave
    opcion=None
    while opcion!=opcion_salida:
        system("cls") #este es para borrar pantalla 
        mostrar_menu(opciones) #este llamara una funcion que haremos mas abajo
        opcion=leer_opcion(opciones)
        ejecutar_opcion(opcion,opciones)
        print() #se imprime para aclarar pantalla

def mostrar_menu(opciones): #con esta funcion mostraremos en pantalla el menu
    print("selecione un opcion: ")
    for clave in sorted(opciones):
        print(f"{clave}) {opciones [clave][0]}" ) #aqui llamamos al diccionario

def leer_opcion(opciones): #aqui leemos la opcion que el usuario nos dio en la funcion de mostrar menu
    while (a:=input("opcion: ")) not in opciones:
        print("opcion incorrecta, vuelva a intentarlo")
    
    return a

def ejecutar_opcion(opcion, opciones): #aqui llamaremos a la funcion nesecesaria segun lo pedido por el menu
    opciones[opcion][1]()

def consultar_asistencia_rut(): #aqui ejecutaremos la opcion 1
    rut_ingreso=input("ingrese el rut del alumno: ") #le pedimos al usuario el rut
    lista_alumnos=obtener_fichero_asistencia()
    valido=False
    for alumnos in lista_alumnos: #con este ciclo se busca el rut deseado
        if rut_ingreso==alumnos["rut"]:
            print(f"el alumno{alumnos['nombre']} tiene una asistencia actual de {alumnos['asistencia_actual']}")
            input()
            valido=True

        if valido==False: #opcion por si no se encuentra
            print(f"el rut {rut_ingreso} no corresponde a ningun alumno")
            input()

def visualiza_asistencia_70(): #aqui llamaremos a la funcion nesecesaria segun lo pedido por el menu
    lista_alumnos=obtener_fichero_asistencia()
    for alumnos in lista_alumnos:
        if alumnos["asistencia_actual"]<70:
            print(f"{alumnos['curso']} alumno {alumnos['nombre']} asistencia {alumnos['asistencia_actual']}")
    input()

def visualiza_asistencia_curso(): #aqui llamaremos a la funcion nesecesaria segun lo pedido por el menu
    curso_ingreso=input("ingrese el curos a revisar: ")
    lista_alumnos=obtener_fichero_asistencia()
    contador_alumnos=0
    for alumnos in lista_alumnos:
        if alumnos["asistencia_actual"]<70 and curso_ingreso==alumnos["curso"]:
            contador_alumnos+=1
    print(f"{curso_ingreso} alumnos con asistencia < 70%: {contador_alumnos}")
    input()

def generar_asistencia_curso(): #aqui llamaremos a la funcion nesecesaria segun lo pedido por el menu
    curso_ingreso=input("ingrese el curso a revisar: ")
    lista_alumnos=obtener_fichero_asistencia()
    with open(r"asistencia_alumnos.csv","w", newline="") as archivo_csv:
        escritor_csv=csv.writer(archivo_csv, delimiter=";")
        escritor_csv.writerow(["curso","nombre","asistencia"])
        for alumnos in lista_alumnos:
            if alumnos["asistencia_actual"] < 70 and curso_ingreso==alumnos["curso"]:
                lista=[]
                lista.append(alumnos["curso"])
                lista.append(alumnos["nombre"])
                lista.append(alumnos["asistencia_actual"])
                escritor_csv.writerow(lista)

def salir():
    print("saliendo")

menu_principal()