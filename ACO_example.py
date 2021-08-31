import numpy as np

from ant_colony import AntColony

distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])
distances2 = np.array([[np.inf, 3, 6, 2, 3],
	                  [3, np.inf, 5, 2 ,3],
	                  [6, 5, np.inf, 6, 4],
	                  [2, 2, 6, np.inf, 6],
	                  [3, 3, 4, 6, np.inf]])

ant_colony = AntColony(distances, 1, 1, 30, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shortest path found: {}".format(shortest_path))

ant_colony2 = AntColony(distances2, 1, 5, 5, 0.5, alpha = 0.7, beta = 0.7)
shortest_path2 = ant_colony2.run()
print("shortest path found: {}".format(shortest_path2))