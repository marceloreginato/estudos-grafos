# Representação de um grafo com dicionário
Grafo = {
    'A': [('B', 2), ('C', 3), ('D', 3)],
    'B': [('A', 2), ('C', 4), ('E', 3)],
    'C': [('A', 3), ('B', 4), ('E', 1), ('F', 6)],
    'D': [('A', 3), ('F', 7)],
    'E': [('B', 3), ('C', 1), ('F', 8)],
    'F': [('C', 6), ('D', 7), ('E', 8), ('G', 9)],
    'F': [('G', 9)],
}

custo = []
prev = []

NIL = -1

for vertice in range(len(Grafo)):
    custo.append(float('inf'))
    print(custo)    
    prev.append(NIL)
custo[0] = 0

