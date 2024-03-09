import matplotlib.pyplot as plt
import networkx as nx

# Definimos la matriz de adyacencia para el grafo a
matriz_a = {
    'a': {'a': 0, 'b': 0, 'c': 1, 'd': 1},
    'b': {'a': 1, 'b': 0, 'c': 1, 'd': 0},
    'c': {'a': 0, 'b': 0, 'c': 0, 'd': 1},
    'd': {'a': 0, 'b': 1, 'c': 1, 'd': 0}
}

# Función para generar un grafo a partir de una matriz de adyacencia
def crear_grafo(matriz):
    G = nx.Graph()
    for nodo, vecinos in matriz.items():
        for vecino, arista in vecinos.items():
            if arista and nodo != vecino:  # Asegurarse de no añadir bucles
                G.add_edge(nodo, vecino)
    return G

# Generamos el grafo a partir de la matriz de adyacencia
G_a = crear_grafo(matriz_a)

# Dibujamos el grafo a
plt.figure(figsize=(6, 6))
nx.draw(G_a, with_labels=True, node_color='skyblue', node_size=1000)
plt.title('Grafo asociado a la tabla a)')
plt.show()