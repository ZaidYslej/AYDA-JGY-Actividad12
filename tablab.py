import networkx as nx
import matplotlib.pyplot as plt

# Función para generar un grafo a partir de una matriz de adyacencia
def crear_grafo(matriz):
    G = nx.Graph()
    for nodo, vecinos in matriz.items():
        for vecino, arista in vecinos.items():
            if arista and nodo != vecino:
                G.add_edge(nodo, vecino)
    return G

# Asegúrate de que esta función está definida antes de llamarla para crear G_b


# Definimos la matriz de adyacencia para el grafo b
matriz_b = {
    'A': {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 0},
    'B': {'A': 1, 'B': 0, 'C': 1, 'D': 0, 'E': 1, 'F': 0},
    'C': {'A': 1, 'B': 0, 'C': 0, 'D': 1, 'E': 0, 'F': 1},
    'D': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 1},
    'E': {'A': 1, 'B': 0, 'C': 1, 'D': 1, 'E': 0, 'F': 1},
    'F': {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 1, 'F': 0}
}

# Generamos el grafo a partir de la matriz de adyacencia
G_b = crear_grafo(matriz_b)

# Realizamos los recorridos DFS y BFS
origen_b = sorted(G_b.nodes())[0]
dfs_b = list(nx.dfs_edges(G_b, source=origen_b))
bfs_b = list(nx.bfs_edges(G_b, source=origen_b))

# Dibujamos el grafo b
plt.figure(figsize=(8, 6))
nx.draw(G_b, with_labels=True, node_color='lightgreen', node_size=1000)
plt.title('Grafo asociado a la tabla b)')
plt.show()

# Imprimimos los recorridos DFS y BFS
print("Recorrido DFS para la tabla b):", dfs_b)
print("Recorrido BFS para la tabla b):", bfs_b)