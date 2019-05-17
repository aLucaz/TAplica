from peas.map import create_map
from peas.map_search_problem import MapSearchProblem


def test_limited():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('104878620', '105012740', pitts_map)
    node_solution, num_visited = iterative_
