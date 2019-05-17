from peas.node import Node


def graph_search(problem, frontier):
    frontier.append(Node(problem.initial))
    explored = set()
    
    while frontier:
        node = frontier.pop()
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node, explored, len(frontier)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
    return None, explored, len(frontier)
