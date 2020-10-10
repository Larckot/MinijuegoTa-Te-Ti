import numpy as np
import random as rd

print('Es hora de jugar al Ta Te Ti')
Ficha = FichaPc = turno = 0
x = True
posicion = ()

tateti = np.array([['_','_','_'],['_','_','_'],['_','_','_']],)

print('El tablero es el siguiente (f son las filas y c las columnas):\n\t\t'
      +str(tateti[0])+'  f1\n\t\t'+str(tateti[1])+'  f2\n\t\t'+str(tateti[2])+'  f3\n\t\t c1  c2  c3\n')

while not (Ficha == 'X' or Ficha == 'O'):
    Ficha = input('Por favor selecciona la ficha deseada entre X y O:').upper()
print('\nComienzan las X.\n')

def empate():
    for x in range(3):
        for y in range(3):
            if tateti[x][y] == '_':
                return False
    print('El juego finalizo en empate.')
    return True

def verificaGanador(ficha,mensaje):
    for x in range(3):
        # Verifica las posibles combinaciones de fila-columna que harian tateti (horizontales, verticales y diagonales)
        if (tateti[x][0] == ficha and tateti[x][1] == ficha and tateti[x][2] == ficha) \
                or (tateti[0][x] == ficha and tateti[1][x] == ficha and tateti[2][x] == ficha) \
                or (tateti[1][1] == ficha and ((tateti[0][0] == ficha and tateti[2][2] == ficha)
                                               or (tateti[0][2] == ficha and tateti[2][0] == ficha))):
            print('TA TE TI !!!\n'+mensaje)
            return True
    return False


def validarFilaColumna():
    y = z = 0
    #Se valida que Z e Y esten entre 1 y 3 que corresponden a las filas y columnas del tablero.
    #Y se manipula excepcion de ValueError por si se ingresa algun valor que no sea numerico
    while not ((y >= 1 and y<=3) and (z >= 1 and z<=3)):
        try:
            y = int(input('Escoja una fila donde posicionar la ficha: '))
            z = int(input('Escoja una columna donde posicionar la ficha: '))
        except ValueError:
            print('Solo se aceptan numeros del 1 al 3')
    posicion = (y-1,z-1)
    return posicion


def validarPosicionLibre(y, z):
    #Se verifica si en la posicion ingresada por el jugador ya hay alguna ficha colocada
    if tateti[y][z] == 'X' or tateti[y][z] == 'O':
        print('Esa posicion no esta libre, por favor vuelva a intentarlo...')
        return True
    return False

def SeleccionPC():
    #Genera otra matriz con los indices de los espacios vacios de la matriz tateti
    coordenadas = np.array(np.where(tateti == '_'))

    #Selecciona aleatoriamente una columna con los valores de fila y columna correspondientes a tateti
    #Y los guarda en SeleccionPC
    posicionAleatoria = int(rd.randint(0, len(coordenadas[0]) - 1))
    SeleccionPC = coordenadas[:, posicionAleatoria]

    #Finalmente inserta la ficha de la PC en la posicion aleatoria.
    tateti[SeleccionPC[0], SeleccionPC[1]] = FichaPC
    return tateti

for turno in range(5):
    # Si el jugador escogio las X comenzara a jugar
    if Ficha == 'X':
        FichaPC = 'O'
        while x == True:
            posicion = validarFilaColumna()
            x = validarPosicionLibre(posicion[0], posicion[1])
        tateti[posicion[0]][posicion[1]] = Ficha
        input('\nUsted ha colocado su ficha.\n' + str(tateti) + '\n Presione ENTER para continuar.\n')
        if verificaGanador(Ficha,'Felicidades has ganado!!!') or empate():
            break
        tateti = SeleccionPC()
        input('\nLa computadora ha puesto su ficha.\n' + str(tateti) + '\n Presione ENTER para continuar.\n')
        if verificaGanador(FichaPC,'Lo siento has perdido...'):
            break
    # Si el jugador escogio las O comenzara la computadora.
    else:
        FichaPC = 'X'
        tateti = SeleccionPC()
        input('La computadora ha puesto su ficha.\n' + str(tateti) + '\n Presione ENTER para continuar.\n')
        if verificaGanador(FichaPC,'Lo siento has perdido...') or empate():
            break
        while x == True:
            posicion = validarFilaColumna()
            x = validarPosicionLibre(posicion[0], posicion[1])
        tateti[posicion[0]][posicion[1]] = Ficha
        input('\nUsted ha colocado su ficha.\n' + str(tateti) + '\n Presione ENTER para continuar.\n')
        if verificaGanador(Ficha,'Felicidades has ganado!!!'):
            break
    turno += 2
    x = True


