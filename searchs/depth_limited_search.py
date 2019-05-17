import sys

from peas.node import Node


def depth_limited_search(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit, set())


def recursive_dls(node, problem, limit, explored_nodes):
    """
    :param explored_nodes: set
    :param limit: int
    :param node: Node
    :type problem: MapSearchProblem
    """
    explored_nodes.add(node)

    if problem.goal_test(node.state):
        return node.solution(), explored_nodes

    elif limit == 0:
        return "cutoff", explored_nodes

    else:
        cutoff_flag = False
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            result, explored_nodes = recursive_dls(child, problem, limit - 1, explored_nodes)

            if result == "cutoff":
                cutoff_flag = True

            elif result is None:
                return result, explored_nodes

        return "cutoff" if cutoff_flag else None, explored_nodes


def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result, explored_nodes = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result
