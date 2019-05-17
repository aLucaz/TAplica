# from matplotlib import pyplot as plt
# import pandas as pd

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.best_first_graph_search import astar_search
from searchs.breadth_first_graph_search import breadth_first_graph_search


def test_best_first_graph_search():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('104878620', '105012740', pitts_map)
    goalNode,  exploredNodes ,frontierNodes = astar_search(pitts_problem)
    
    
    rute = goalNode.solution()
    print("Ruta encontrada: ")
    for node in rute: 
        print(node)
    print("META")
    print("Costo de la ruta encontrada: {} Km".format(goalNode.path_cost))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Número de nodos visitados: {}".format(len(exploredNodes)))
    print("Número de nodos en memoria: {}".format(len(exploredNodes) + frontierNodes))
