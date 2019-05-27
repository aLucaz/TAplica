
from searchs.best_first_graph_search import astar_search


def test_best_first_graph_search(problem):
    goal_node,  explored_nodes, frontier_nodes = astar_search(problem)

    rute = goal_node.solution()

    print("Costo de la ruta encontrada: {} Km".format(goal_node.path_cost))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Número de nodos visitados: {}".format(len(explored_nodes)))
    print("Número de nodos en memoria: {}".format(len(explored_nodes) + frontier_nodes))
