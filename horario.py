from typing import List,Tuple

def sacar_turno(m: List[List[str]],dias: Tuple[str],hora: Tuple[str],pacientes_validos: List[str]) -> None:
    '''Reserva el turno deseado

    Pre: Recibe tuplas de los días y horarios, junto con una matriz que contiene los turnos ya reservados.
    Tambien recibe una lista con los pacientes validos
    
    Post: En caso de estar disponible el turno seleccionado, modifica la matriz con los turnos para reservar el turno del paciente
    '''
    idxud=[]
    idxuh=[]
    while True:
        print('¿Qué día quiere reservar el turno?')
        print('|',end='')
        for idx,dia in enumerate(dias, start=1):
            print(f' {idx}- {dia} ', end='|')
            idxud.append(str(idx))
        print()
        ud= input('Ingrese el número correspondiente al día: ')
        if ud not in idxud:
            print('Ingreso un día invalido, por favor intente de nuevo')
        else:
            break
    
    #Seleccion de la hora
    while True:
        print('¿Qué hora quiere reservar?')
        print('|',end='')
        for ind,hs in enumerate(hora,start=1):
            print(f' {ind}- {hs}hs ', end='|')
            idxuh.append(str(ind))
        print()
        uh= input('Ingrese el número correspondiente a la hora deseada: ')
        if uh not in idxuh:
            print('Ingreso una hora invalida, por favor intente de nuevo')
        else:
            break
    
    #Reservación del turno
    turno= m[int(ud)-1][int(uh)-1]
    if turno not in tuple(f"{hora:02}:{minuto:02}" for hora in range(8, 13) for minuto in range(0, 60, 30)):
        print('El turno ya está reservado')
    else:
        up= input('Ingrese el nombre y apellido del paciente: ')
        if up.upper() in pacientes_validos:
            print(f'Reservo turno para el dia {dias[int(ud)-1]} a las {hora[int(uh)-1]} para el paciente {up}')
            m[int(ud)-1][int(uh)-1]= up
        else:
            print(f'El paciente {up} no está registrado. Si desea cargarlo al sistema utilice la opción 1')
   
