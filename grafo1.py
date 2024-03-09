import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo basado en la imagen proporcionada
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'), ('B', 'F'), 
    ('C', 'G'), ('C', 'H'), 
    ('D', 'I'), ('D', 'J'),
    ('E', 'K'), 
    ('F', 'L'), ('F', 'M')
])

# Recorrido en profundidad (DFS)
dfs_paths = list(nx.dfs_edges(G, source='A'))

# Recorrido en anchura (BFS)
bfs_paths = list(nx.bfs_edges(G, source='A'))

# Dibujar el grafo para visualizarlo
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000)
plt.title('Recorrido de Grafo')
plt.show()

# Imprimir los recorridos
print("Recorrido en profundidad (DFS) desde 'A':", dfs_paths)
print("Recorrido en anchura (BFS) desde 'A':", bfs_paths)
