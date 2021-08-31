#author:Roqaiyya Mahmood, code for plotting tsp optimal tour on the problem graph
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
G = nx.Graph()
distances2 = np.array([[np.inf, 3, 6, 2, 3],
	                  [3, np.inf, 5, 2 ,3],
	                  [6, 5, np.inf, 6, 4],
	                  [2, 2, 6, np.inf, 6],
	                  [3, 3, 4, 6, np.inf]])

for i in range(0,len(distances2[0])):
	for j in range(i,len(distances2[0])):
		if j == i :
			continue
		G.add_edge(i,j, weight = distances2[i][j],color='lightgreen')

tours = [([(0, 3), (3, 4), (4, 1), (1, 2), (2, 0)], 22.0),
         ([(0, 4), (4, 2), (2, 3), (3, 1), (1, 0)], 18.0),
         ([(0, 2), (2, 3), (3, 1), (1, 4), (4, 0)], 20.0),
         ([(0, 3), (3, 1), (1, 4), (4, 2), (2, 0)], 17.0),
         ([(0, 4), (4, 2), (2, 3), (3, 1), (1, 0)], 18.0)]
         
for i in range(0,len(tours)):
	tup = tours[i]
	x1 = tup[0]
    path = []
    for a in x1:
		path.append(a[0])
	path.append(x1[0][0])
	print(path)

	for i in range(0,len(path)-1):
		G.add_edge(path[i],path[i+1],color='r',width=3.0,arrows=True)


	colors = nx.get_edge_attributes(G,'color').values()
	weights = nx.get_edge_attributes(G,'weight').values()
	pos = nx.circular_layout(G)

	nx.draw(G, edge_color = colors, with_labels=True,node_color='lightblue')
	plt.xlabel("x coordinates of cities")
	plt.ylabel("y coordinates of cities")
	plt.title("Symmetric TSP for ACO")
	plt.savefig("Iteration {iter} plot.png".format(i))



