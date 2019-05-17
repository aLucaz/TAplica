from peas.node import Node
from peas.prio_queue import Frontier


def best_first_graph_search(problem, fn):
    """
    Si f es node.depth tenemos Busqueda en Amplitud; 
    si f es node.path_cost tenemos Busqueda  de Costo Uniforme.
    Si f es una heurística tenemos Busqueda Voraz;
    Si f es node.path_cost + heuristica(node) tenemos A* """

    frontier = Frontier(fn)
    frontier.add(Node(problem.initial))
    explored = set()
    
    while frontier:
        node = frontier.pop()
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node, explored, len(frontier)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and child not in frontier:
                frontier.add(child)
            elif child in frontier:
                if fn(child) < frontier[child]:
                    frontier.replace(child)
    
    return None, explored, len(frontier)


def astar_search(problem):
    fn = lambda node: node.path_cost + problem.map.heuristics[str(node.state)]
    return best_first_graph_search(problem, fn)
