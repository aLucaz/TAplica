from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.depth_graph_search import depth_graph_search


def test_depth_graph_search():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('104878620', '105012740', pitts_map)
    goalNode, exploredNodes , frontierLengthNodes= depth_graph_search(pitts_problem)
        
    rute = goalNode.solution()
    print("Ruta encontrada: ")
    for node in rute: 
        print(node)
    print("META")
    print("Número de nodos visitados: {}".format(len(exploredNodes)))
    print("Número de nodos en memoria: {}".format(len(exploredNodes) + frontierLengthNodes))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Costo de la ruta encontrada: {} Km".format(goalNode.path_cost))