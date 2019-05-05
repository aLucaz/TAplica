from collections import deque
from peas.node import Node


def breadth_first_graph_search(problem):
    visited_nodes = []
    node = Node(problem.initial)
    visited_nodes.append(node)

    if problem.goal_test(node.state):
        return node, visited_nodes

    frontier = deque([node])
    explored = set()

    while frontier:
        node = frontier.pop() 
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child, visited_nodes
                frontier.append(child)

    return None, visited_nodes
