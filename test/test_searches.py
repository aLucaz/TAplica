# from matplotlib import pyplot as plt
# import pandas as pd

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.best_first_graph_search import astar_search
from searchs.breadth_first_graph_search import breadth_first_graph_search


def test_breadth():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('104878620', '105012740', pitts_map)
    # solNode, exploredNodes = astar_search(pittsProblem)
    sol_node, explored_nodes = breadth_first_graph_search(pitts_problem)
    print("node state: ", sol_node.state)
    print("way: ")
    [print(node) for node in sol_node.solution()]
