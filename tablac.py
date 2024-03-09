import networkx as nx
import matplotlib.pyplot as plt

# Definimos la matriz de adyacencia para el grafo c
matriz_c = {
    'V': {'V': 0, 'W': 1, 'X': 1, 'Y': 1, 'Z': 0},
    'W': {'V': 1, 'W': 0, 'X': 1, 'Y': 0, 'Z': 1},
    'X': {'V': 1, 'W': 0, 'X': 0, 'Y': 1, 'Z': 0},
    'Y': {'V': 1, 'W': 1, 'X': 1, 'Y': 0, 'Z': 1},
    'Z': {'V': 0, 'W': 1, 'X': 0, 'Y': 1, 'Z': 0}
}

# Asegúrate de que la función crear_grafo() esté definida en tu entorno de trabajo.
# Aquí está la definición por si necesitas copiarla de nuevo:
def crear_grafo(matriz):
    G = nx.Graph()
    for nodo, vecinos in matriz.items():
        for vecino, arista in vecinos.items():
            if arista and nodo != vecino:
                G.add_edge(nodo, vecino)
    return G

# Generamos el grafo a partir de la matriz de adyacencia
G_c = crear_grafo(matriz_c)

# Realizamos los recorridos DFS y BFS
origen_c = sorted(G_c.nodes())[0]
dfs_c = list(nx.dfs_edges(G_c, source=origen_c))
bfs_c = list(nx.bfs_edges(G_c, source=origen_c))

# Dibujamos el grafo c
plt.figure(figsize=(8, 6))
nx.draw(G_c, with_labels=True, node_color='lightcoral', node_size=1000)
plt.title('Grafo asociado a la tabla c)')
plt.show()

# Imprimimos los recorridos DFS y BFS
print("Recorrido DFS para la tabla c):", dfs_c)
print("Recorrido BFS para la tabla c):", bfs_c)