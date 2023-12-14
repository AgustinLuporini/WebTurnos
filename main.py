#LIBRERIAS
import paciente as pc
import horario as hs
import turnero
from typing import List,Tuple

#MANEJO DE ARCHIVOS-----------
def abrir_arch(nombre: str) -> List[List[str]]:
    '''Abre un archivo .csv

    Pre: Recibe el nombre del archivo
    
    Post: Retorna una matriz con todos los datos del archivo
    '''
    salida=[]
    try:
        with open(nombre,'rt',encoding='utf-8-sig') as arch:
            for linea in arch:
                salida.append(linea.rstrip().split(';'))
    except FileNotFoundError:
        print(f'Aún no existe el archivo {nombre}. Creelo con la opción 1 para pacientes, y la 3 para turnos')
    except:
        print(f'Ocurrio un problema con el archivo {nombre}')
    return salida

def export_arch_at(nombre: str,matriz: List[List[str]]) -> None:
    '''Agrega información a un archivo ya existente o lo crea de ser necesario

    Pre: Recibe el nombre del archivo y una matriz
    
    Post: Agrega los datos de la matriz al archivo
    '''
    try:
        with open(nombre,'at',encoding='utf-8-sig') as arch:
            for lista in matriz:
                txt=';'.join(lista)
                arch.write(txt + '\n')
    except:
        print('No se pudo guardar los cambios')
        
        
def export_arch_wt(nombre: str,m: List[List[str]]):
    '''Crea un archivo nuevo y le escribe los datos de una matriz

    Pre: Recibe el nombre del archivo y la matriz
    
    Post: Exporta el archivo con los datos de la matriz
    '''
    try:
        with open(nombre,'wt',encoding='utf-8-sig') as arch:
            for linea in m:
                txt= ';'.join(linea) + '\n'
                arch.write(txt)
    except Exception as e:
        print('No se pudo exportar el archivo')
        
#-----------------
#OPCIONES DEL MENÚ------------------

def opciones() -> None:
    '''Imprime las opciones del menú

    Pre: -
    
    Post: Imprime las opciones
    '''
    opc= ('Menú de opciones',
          '1-Crear nuevo paciente',
          '2-Reservar turnos',
          '3-Crear/Reiniciar turnos',
          '4-Ver turnos',
          '5-Ver pacientes',
          '0-Para salir'
          )
    for i in opc:
        print(i)
    print()


def opc1(pacientes: List[List[str]],obras_validas: Tuple[str],paci_cargados: List[str],tel_cargados: List[str],dni_cargados: List[str]) -> None:
    '''Crea un nuevo paciente

    Pre: -Pacientes es una matriz que contiene todos los pacientes con sus datos
         -Obras validas es una tupla que contiene las obras sociales con las que trabaja el laboratoio
         -Paci_cargados,tel_cargados y dni_cargados son listas que contienen los nombres y apeliido,telefonos y DNI ya asociados a un paciente
    
    Post: Guarda los datos del nuevo paciente en la lista de pacientes
    '''
    while True:
        nombre=pc.crear_nombre()
        obra=pc.crear_obra_social(obras_validas)
        tel=pc.crear_telefono(tel_cargados)
        dni=pc.crear_dni(dni_cargados)
        print('¿Quiere registrar al siguiente paciente?:')
        print(f'Nombre: {nombre}\nObra social: {obra}\nTelefono: {tel}\nDNI: {dni}') 
        u= input('Ingrese 1 si los datos son correctos: ')
        if u == '1':
            break
    pacientes.append([nombre,obra,tel,dni])
    paci_cargados.append(nombre.upper())
    tel_cargados.append(tel)
    dni_cargados.append(dni)
    print('Se registro al paciente de manera exitosa')
    
    
def opc2(matriz: List[List[str]],dias: Tuple[str],horas: Tuple[str], pacientes: List[str]) -> None:
    '''Reserva los turnos a un paciente unicamente si los turnos ya han sido creados

    Pre: -Recibe una matriz con todos los turnos de la semana
         -Recibe tuplas que contienen los días y las horas en las que se pueden resevar turnos
         -Recibe una lista de los pacientes ya creados
         
    Post: -Si los turnos no fueron creados imprime un mensaje indicandolo
          -Si el paciente no existe lo avisa
          -Si nada de lo anterior ocurre, se le reserva el turno a un paciente especifico
    '''
    if not matriz:
        print('Los turnos no han sido creados. Ejecute la opción 3')
        return
    hs.sacar_turno(matriz,dias,horas,pacientes)
    print()
    

def opc3() -> None:
    '''Crear/Reiniciar los turnos

    Pre: -
    
    Post: Se crea un archivo csv que contiene todos los turnos y se retorna una matriz con estos mismos
    '''
    m=turnero.crear('turnos.csv')
    print('¡Se han creado los nuevos turnos de manera exitosa!')
    print('Salga del programa y vuelva a entrar para seguir trabajando.')
    return m


        
def opc_print(pacientes: List[List[str]]) -> None:
    '''Imprime los pacientes junto con su información

    Pre: Recibe una matriz que contiene los datos de cada paciente
    
    Post: Imprime los pacientes y sus datos
    '''
    for paciente in pacientes:
        print('| ',end='')
        print(' | '.join(paciente),'|')
  
#------------
#MENÚ---------
def menu() -> None:
    '''Menú para ejecutar todas las opciones del programa

    Pre: -
    
    Post: Se ejecutan las opciones que el usuario desee. Ni bien se ejecuta el menú se abren todos los archivos
    para trabajar sore estos y recien una cuando el usuario cierra el programa se exporta la nueva información
    a cada archivo
    '''
    dias= ('Lunes','Martes','Miercoles','Jueves','Viernes')
    horas= tuple(f'{hora:02}:{minutos:02}' for hora in range(8,13) for minutos in range(00,60,30))
    obras_validas=('OSDE','SWISS MEDICAL', 'GALENO', 'MEDIFE', 'PAMI','IOMA')
    pacientes= abrir_arch('pacientes.csv')
    horarios= abrir_arch('turnos.csv')
    pacientes_cargados= [paciente[0].upper() for paciente in pacientes]
    tel_cargados= [tel[2] for tel in pacientes]
    dni_cargados= [dni[3] for dni in pacientes]
    while True:
        print()
        opciones()
        u= input('Ingrese la opción que desea ejecutar: ')
        print()
        if u == '1':
            opc1(pacientes,obras_validas,pacientes_cargados,tel_cargados,dni_cargados)
        elif u == '2':
            opc2(horarios,dias,horas,pacientes_cargados)
        elif u == '3':
            horarios= opc3()
        elif u == '4':
            if horarios:
                print('Lista de horarios:')
                opc_print(horarios)
            else:
                print('Los turnos no han sido creados. Ejecute la opción 3.')
        elif u == '5':
            if pacientes:
                print('Lista de pacientes:')
                opc_print(pacientes)
            else:
                print('No hay ningún paciente registrado')
        elif u == '0':
            break
        else:
            print('Error, ingrese una opción valida.')
        print()
    export_arch_at('pacientes.csv',pacientes)
    export_arch_wt('turnos.csv',horarios)
        
        
        
#CODIGO GENERAL--------
if __name__ == '__main__':
    menu()