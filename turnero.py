from typing import List

def crear(nombre: str) -> List[List[str]]:
    '''Crea un archivo con todos los horario de atención de la clinica

    Pre: Recibe el nombre con el que se creará el archivo
    
    Post: Crea un archivo csv con los horarios y retorna una matriz con los mismos
    '''
    salida=[]
    try:
        with open(nombre, 'wt', encoding='utf-8-sig') as arch:
            for i in range(5):
                dia= tuple(f"{hora:02}:{minuto:02}" for hora in range(8, 13) for minuto in range(0, 60, 30))
                arch.write(';'.join(dia) + '\n')
                salida.append(list(dia))
    except:
        print('No se puedieron crear los turnos')
    return salida

