#  Prova Escrita 3 - Fet per Álvaro Gómez Fernández

m1 = 10.50
m2 = 12.00
m3 = 15.00

notes_estudiants = {
    "Anna": {"Matemàtiques": 8, "Història": 7},
    "Marc": {"Matemàtiques": 6},
    "Laura": {"Ciències": 9, "Matemàtiques": 10},
    "Jordi": {"Història": 5},
}

# Exercici 1:

def trobar_millor_pitjor_rendiment(*nombres):
    if len(nombres) != 0:
        millor = min(nombres)
        pitjor = max(nombres)
        
        return millor, pitjor
    else:
        return 0, 0

# millor, pitjor = trobar_millor_pitjor_rendiment(m1, m2, m3)
# print(f"La millor marca de {m1}, {m2}, {m3} és {millor} i la pitjor és {pitjor}")

# Exercici 2:

def comptar_estudiants(estudiants):
    nombre_estudiants = len(estudiants)
    return nombre_estudiants

# nombre_estudiants = comptar_estudiants(notes_estudiants)
# print(f"Hi ha {nombre_estudiants} estudiants matriculats a l'institut.")

# Exercici 3:

def comptar_estudiants_matèria(notes, matèria):
    nombre_estudiants_matriculats = 0
    for estudiant in notes:
        if matèria in notes[estudiant]:
            nombre_estudiants_matriculats += 1
    return nombre_estudiants_matriculats    

# nombre_estudiants_matriculats = comptar_estudiants_matèria(notes_estudiants, "Matemàtiques")
# print(f"Hi ha {nombre_estudiants_matriculats} estudiant(s) matriculat(s) a la matèria Matemàtiques.")

# Exercici 4:

def mostrar_estudiants_matèries(notes):
    
    materies = set()
    for estudiant in notes:
        materies.update(notes[estudiant].keys())
    for materia in materies:
        print(f"Hi ha {comptar_estudiants_matèria(notes, materia)} estudiant(s) matriculat(s) a la matèria {materia}.")
            
# mostrar_estudiants_matèries(notes_estudiants)

# Fet per Álvaro Gómez Fernández