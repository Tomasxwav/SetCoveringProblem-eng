#############################################################################################
import time
dataset = input("Inserta el nombre del archivo a leer: ")
#############################################################################################
# Funcion para guardar los datos del archivo .txt en un array
def process_data():
    with open(f"dataset/{dataset}.txt", 'r') as file:
        lines = file.read().splitlines()  # divide por lineas el archivo
        numbers = []
        for line in lines:
            line_numbers = list(map(int, line.split()))
            numbers += line_numbers
        return numbers
numbers = process_data()
#############################################################################################
#############################################################################################

"El primer dato del arreglo dice # de filas (m) y el segundo # de columnas (n)"
m_filas = numbers[0]
n_columnas = numbers[1]
numbers = numbers[2:]  # eliminar los primeros 2 datos del arreglo con el metodo slicing ya que no los usaremos

#############################################################################################
#############################################################################################

"Creamos el conjunto universo (en este caso seran ´m´ elementos)"
Universe = [i for i in range(1, m_filas+1)]

#############################################################################################
#############################################################################################

"Los primeros 'n' elementos del txt son el costo de cada columna/subset (n) "
Cost = []
for i in range(n_columnas):
    Cost.append(numbers[i])
numbers = numbers[n_columnas:]  # Los eliminamos del array

Costos = Cost
#############################################################################################
#############################################################################################
"Creamos los arreglos de las columnas que cubren la fila i"
columns = []
for i in range(m_filas):
    subset = []
    for j in range(numbers[0]):
        subset.append(numbers[j + 1])
    numbers = numbers[numbers[0] + 1:]  # los eliminamos del array
    columns.append(subset)
Columnas_arr = columns
Columnas = [set(s) for s in columns]

#Imprimimos
"""print("Arreglos de las columnas que cubren la fila i")
print(Columnas_arr)"""
#############################################################################################
#############################################################################################
"""print("==================MATRIZ Aij===================")
print("r/c 1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10")"""
A = []
for i in range(m_filas):
    a = []
    for j in range(n_columnas):
        a.append(0)
        for k in range(len(Columnas_arr[i])):
            if Columnas_arr[i][k] == j+1:
                a.append(1)
                a = a[:-2] + a[-1:]
    A.append(a)

"""for i in range(m_filas):
    print(f"{i+1}: {A[i]}")"""
#############################################################################################
#############################################################################################
"==================CREAR LOS SUBSETS=================="
Subsets = []
for n in range(n_columnas):
    s = []
    for m in range(m_filas):
        if A[m][n] == 1:
            s.append(m+1)
    Subsets.append(s)
subsets = [set(s) for s in Subsets]
#Imprimir
"""print("==================CREANDO LOS SUBSETS==================")
print(Subsets)"""
#############################################################################################
#############################################################################################
print("==================RESULTADO==================")
universe = set(Universe)
costo_temp = 0
costo_tot = 0
selected_subsets = []
index = []
seleccionado = set()
seleccionado_index = 0
seleccionados_costos = []
avr_mayor = 0
i = 0
while universe != set():
    seleccionado = subsets[i]
    avr_mayor = len(universe & subsets[0]) / Costos[0]
    for j in range(len(subsets)):
        if avr_mayor <= (len(universe & subsets[j]) / Costos[j]):
            avr_mayor = (len(universe & subsets[j]) / Costos[j])
            seleccionado = subsets[j]
            costo_temp = Costos[j]
            seleccionado_index = j
            #print(f"{j+1}- avr_mayor: {avr_mayor}, subset: {seleccionado}, costo: {costo_temp}")
    #print(f"universe antes: {universe}")
    universe -= seleccionado
    #print(f"Selected {i+1}: {seleccionado}")
    selected_subsets.append(seleccionado)
    index.append(seleccionado_index)
    seleccionados_costos.append(costo_temp)
    costo_tot += costo_temp
    #print(f"universe desp: {universe}")
    i += 1

print(f"Costo total: {costo_tot}")
print("Costo optimo conocido: 492")
print(f"Tu % de error es de: {round(100*((costo_tot-492)/492),2)} %")
print(f"Los {len(selected_subsets)} subsets seleccionados son: ")
for i in range(len(selected_subsets)):
    print(f"{i+1}: {index[i]+1} {selected_subsets[i]}, ${seleccionados_costos[i]}")




