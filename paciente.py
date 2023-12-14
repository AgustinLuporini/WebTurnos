import re
from typing import List

def verificar_nombre(nombre: str) -> bool:
    '''Recibe un string y verifica si contiene unicamente letras

    Pre: Recibe un string
    
    Post: Devuelve un valor booleano. True si el nombre ingresado es valido, y False en caso contrario
    '''
    valido= r'^[a-zA-Z\s]+$'
    if len(nombre)<3 or len(nombre)>10:
        return False
    if re.match(valido,nombre):
        return True
    return False

def crear_nombre() -> str:
    '''Crea y retorna el nombre del paciente a cargar

    Pre: -
    
    Post: Retorna un nombre de paciente valido
    '''
    nombre= input('Ingrese nombre y apellido del paciente a registrar:')
    while verificar_nombre(nombre) == False:
        print('El nombre ingresado no es valido. Intente de nuevo.')
        nombre= input('Ingrese el nombre del paciente a registrar:')
    return nombre
    
def crear_obra_social(obras_validas: List[str]) -> str:
    '''Devuelve la obra social del paciente

    Pre: Recibe un lista de las obras sociales con las que trabaja la clinica
    
    Post: Retorna la obra social del paciente
    '''
    while True:
        obra= input('Ingrese la obra social del paciente: ').upper()
        if obra not in obras_validas:
            print('El laboratorio no trabaja con esa obra social')
        else:
            break
    return obra

def crear_telefono(tel_cargados: List[int]) -> str:
    '''Devuelve un número de telefono unico para el paciente

    Pre: Recibe una lista con los telefonos ya registrados
    
    Post: Retorna el telefono del paciente
    '''
    while True:
        telefono= input('Ingrese el telefono del paciente: ')
        if len(telefono)<5 or len(telefono)>15:
            print('El telefono ingresado no es valido')
            continue
        elif not telefono.isdigit():
            print('Ingrese números unicamente')
        elif telefono in tel_cargados:
            print('El telefono ingresado ya existe')
        else:
            return telefono


  

def crear_dni(dni_cargados: List[int]) -> str:
    '''Devuelve un número de DNI unico para el paciente

    Pre: Recibe una lista con los DNI ya registrados
    
    Post: Retorna el DNI del paciente
    '''
    while True:
        dni= input('Ingrese el DNI del paciente: ')
        if len(dni)<8 or len(dni)>11:
            print('El DNI ingresado no es valido')
            continue
        elif not dni.isdigit():
            print('Ingrese números unicamente')
        elif dni in dni_cargados:
            print('El DNI ingresado ya existe')
        else:
            return dni
