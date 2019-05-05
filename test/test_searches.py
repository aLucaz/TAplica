# from matplotlib import pyplot as plt
# import pandas as pd

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.best_first_graph_search import astar_search
from searchs.breadth_first_graph_search import breadth_first_graph_search


def test_breadth():
    pittsMap = create_map()
    pittsProblem = MapSearchProblem('104878620', '105012740', pittsMap)
    # solNode, exploredNodes = astar_search(pittsProblem)
    solNode, exploredNodes = breadth_first_graph_search(pittsProblem)
