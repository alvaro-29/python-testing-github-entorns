# Prova Escrita 4 - Fet per Álvaro Gómez Fernández

m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Exercici 1:

def cercar_el(matriu: list, element: int, mostrar_posicio: bool = False):
    trobat = False
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == element:
                trobat = True
                if mostrar_posicio:
                    return (trobat, (i,j))
                else:
                    return (trobat, None)
    return (trobat, None)

#print(cercar_el(m_ex, 5, True))

# Exercici 2:

def sumar_fila(matriu: list, index = 0):
    suma = 0
    for i in range(len(matriu)):
        if i == index:
            for j in range(len(matriu[i])):
                suma = suma + matriu[i][j]
            return suma
    return 0

# print(sumar_fila(m_ex, 2))
# print(sumar_fila(m_ex, 10))

# Exercici 3:

def sumar_matriu(matriu: list):
    suma = 0
    for i in range(len(matriu)):
        suma = suma + sumar_fila(matriu, i)
    return suma

# print(sumar_matriu(m_ex))

# Exercici 4:

def transformar(matriu: list, k: int, op: str = "+"):
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if op == "+":
                matriu[i][j] += k
            elif op == "-":
                matriu[i][j] -= k
            elif op == "+*":
                matriu[i][j] *= k
            elif op == "/":
                matriu[i][j] /= k
      

# transformar(m_ex, 10, "+")

# Fet per Álvaro Gómez Fernández