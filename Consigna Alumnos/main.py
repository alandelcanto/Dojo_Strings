from os import system
from data import lista_videos
from class_video import Video

"""
Integrantes:

Agustín Gonzalez
Alan del Canto
Alex Fernández
Celeste Czajkowski



Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFGH no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""


normalizado = False

error_normalizacion = "No se normalizaron los videos, por favor seleccione la opcion A"

while True:
    opcion: str = input("Seleccione una de las siguientes opciones:\nA. NORMALIZAR OBJETOS\nB. MOSTRAR TEMAS\nC. ORDENAR TEMAS\nD. PROMEDIO DE VISTAS\nE. MAXIMA REPRODUCCION\nF. BUSQUEDA POR CODIGO\nG. LISTAR POR COLABORADOR\nH. LISTAR POR MES\nI. SALIR\n")
    opcion = opcion.upper()
    match opcion:
        case "A":
            Video.normalizar_objetos(Video, lista_videos)
            normalizado = True
        case "B":
            if normalizado:
                Video.mostrar_lista_temas(Video, lista_videos)
            else:
                print(error_normalizacion)
        case "C":
            if normalizado:
                Video.ordenar_temas(Video, lista_videos)
            else:
                print(error_normalizacion)
        case "D":
            if normalizado:
                Video.promedio_vistas(Video, lista_videos)
            else:
                print(error_normalizacion)
        case "E":
            if normalizado:
                Video.maxima_reproduccion(Video, lista_videos)
            else:
                print(error_normalizacion)
        case "F":
            if normalizado:
                codigo: str = input("Por favor ingrese el codigo: \n")
                Video.busqueda_por_codigo(Video, lista_videos, codigo)
            else:
                print(error_normalizacion)
        case "G":
            if normalizado:
                colaborador: str = input("Por favor ingrese el colaborador: \n")
                Video.listar_por_colaborador(Video, lista_videos, colaborador)
            else:
                print(error_normalizacion)
        case "H":
            if normalizado:
                mes: str = input("Por favor ingrese el mes: \n")
                Video.listar_por_mes(Video, lista_videos, mes)
            else:
                print(error_normalizacion)
        case "I":
            break
        case _:
            print("Por favor ingrese una opcion valida")
        
    system("pause")
    system("cls")