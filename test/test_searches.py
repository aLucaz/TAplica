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
    solNode, exploredNodes = breadth_first_graph_search(pitts_problem)
