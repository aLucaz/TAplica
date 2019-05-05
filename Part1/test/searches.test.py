# from matplotlib import pyplot as plt
# import pandas as pd

from Part1.peas.map import create_map
from Part1.peas.map_search_problem import MapSearchProblem
from Part1.searchs.best_first_graph_search import astar_search

if __name__ == "__main__":
    pittsMap = create_map()
    print(pittsMap.heuristics['1'])
    pittsProblem = MapSearchProblem('104878620', '105012740', pittsMap)
    solNode, exploredNodes = astar_search(pittsProblem)
