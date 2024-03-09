import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo basado en el Grafo #2 proporcionado
G2 = nx.Graph()
G2.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'), 
    ('C', 'F'), ('C', 'G'), ('C', 'H'),
    ('D', 'I'), ('D', 'J'),
    ('E', 'K'), ('E', 'L'),
    ('H', 'M')
])

# Realizar el recorrido en profundidad (DFS)
dfs_paths_g2 = list(nx.dfs_edges(G2, source='A'))

# Realizar el recorrido en anchura (BFS)
bfs_paths_g2 = list(nx.bfs_edges(G2, source='A'))

# Dibujar el grafo para visualizarlo
plt.figure(figsize=(8, 6))
nx.draw(G2, with_labels=True, node_color='skyblue', node_size=1000, font_size=16)
plt.title('Grafo #2')
plt.show()

# Imprimir los recorridos DFS y BFS
print("Recorrido DFS en Grafo #2:", dfs_paths_g2)
print("Recorrido BFS en Grafo #2:", bfs_paths_g2)