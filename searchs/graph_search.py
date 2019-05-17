from peas.node import Node


def graph_search(problem, frontier):
    frontier.append(Node(problem.initial))
    explored = set()
    visited_nodes = []

    while frontier:
        node = frontier.pop()
        visited_nodes.append(node)
        if problem.goal_test(node.state):
            return node, visited_nodes
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
    return None, visited_nodes, len(frontier)
