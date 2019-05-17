from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.depth_limited_search import iterative_deepening_search


def test_limited():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('104878620', '105012740', pitts_map)
    goal_node, explored = iterative_deepening_search(pitts_problem)

    rute = goal_node.solution()

    print("Número de nodos visitados: {}".format(sum(explored)))
    print("Número de nodos en memoria: {}".format(explored.pop()))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Costo de la ruta encontrada: {} Km".format(goal_node.path_cost))
    print("Profundidad de búsqueda: {}".format(len(explored)))
