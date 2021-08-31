#author:Roqaiyya Mahmood, code for plotting a symmetric graph from given distance matrix
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
G = nx.Graph()
distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])
for i in range(0,len(distances[0])):
	for j in range(i,len(distances[0])):
		if j == i :
			continue
		G.add_edge(i,j, weight = distances[i][j],color='lightgreen')
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
#pos = nx.circular_layout(G)

nx.draw(G, edge_color = colors, width=list(weights), with_labels=True,node_color='lightblue')
plt.xlabel("x coordinates of cities")
plt.ylabel("y coordinates of cities")
plt.title("Symmetric TSP for ACO")
plt.show()