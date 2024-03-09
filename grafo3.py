import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo basado en el Grafo #3 proporcionado
G3 = nx.Graph()
G3.add_edges_from([
    (1, 2), (1, 3),
    (2, 4), (3, 4),
    (4, 5), (4, 6),
    (5, 7), (6, 7)
])

# Realizar el recorrido en profundidad (DFS)
dfs_paths_g3 = list(nx.dfs_edges(G3, source=1))

# Realizar el recorrido en anchura (BFS)
bfs_paths_g3 = list(nx.bfs_edges(G3, source=1))

# Dibujar el grafo para visualizarlo
plt.figure(figsize=(8, 6))
nx.draw(G3, with_labels=True, node_color='salmon', node_size=1000, font_size=16)
plt.title('Grafo #3')
plt.show()

# Imprimir los recorridos DFS y BFS
print("Recorrido DFS en Grafo #3:", dfs_paths_g3)
print("Recorrido BFS en Grafo #3:", bfs_paths_g3)