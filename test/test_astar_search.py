# from matplotlib import pyplot as plt
# import pandas as pd

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.best_first_graph_search import astar_search


def test_astar_search():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('656071251', '105012740', pitts_map)
    goal_node, visited_nodes, frontier_nodes = astar_search(pitts_problem)

    rute = goal_node.solution()

    print("Costo de la ruta encontrada: {} Km".format(goal_node.path_cost))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Número de nodos visitados: {}".format(len(visited_nodes)))
    print("Número de nodos en memoria: {}".format(len(visited_nodes) + frontier_nodes))
