from Part1.peas.node import Node
from Part1.peas.prio_queue import Frontier


def best_first_graph_search(problem, fn):
    """
    Busca el objetivo expandiendo el nodo de la frontera con el menor valor de la funcion f.     
    Memoriza estados visitados
    Antes de llamar a este algoritmo hay que especificar La funcion f(node). 

    Si f es node.depth tenemos Busqueda en Amplitud; 
    si f es node.path_cost tenemos Busqueda  de Costo Uniforme.
    Si f es una heurística tenemos Busqueda Voraz;
    Si f es node.path_cost + heuristica(node) tenemos A* """

    frontier = Frontier(fn)
    frontier.add(Node(problem.initial))
    explored = set()
    visited_nodes = []

    while frontier:
        node = frontier.pop()
        visited_nodes.append(node)
        if problem.goal_test(node.state):
            return node, visited_nodes
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and child not in frontier:
                frontier.add(child)
            elif child in frontier:
                if fn(child) < frontier[child]:
                    frontier.replace(child)
    return None, visited_nodes


def astar_search(problem):
    """ Algoritmo A*, un caso especial de best_first_graph_search con f = path_cost + heuristic  """
    fn = lambda node: node.path_cost + problem.map.heuristics[str(node.state)]
    return best_first_graph_search(problem, fn)
