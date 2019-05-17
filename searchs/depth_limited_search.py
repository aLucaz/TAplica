import sys

from peas.node import Node


def depth_limited_search(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit, [])


def recursive_dls(node, problem, limit, visited_nodes):
    """
    :param limit: int
    :param node: Node
    :type problem: MapSearchProblem
    """
    visited_nodes.append(node)

    if problem.goal_test(node.state):
        return node.solution(), cant_visited + 1

    elif limit == 0:
        return "cutoff", cant_visited + 1

    else:
        cutoff_flag = False
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            result = recursive_dls(child, problem, limit - 1, cant_visited)

            if result == "cutoff":
                cutoff_flag = True

            elif result is None:
                return result

        return "cutoff" if cutoff_flag else None


def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result, cant_visited = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result
