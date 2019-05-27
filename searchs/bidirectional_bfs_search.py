from peas.fifo_queue import FIFOQueue
from peas.node import Node


def bidirectional_search(problem):
    frontier_f = FIFOQueue()
    frontier_b = FIFOQueue()

    explored_f = set()
    explored_b = set()

    frontier_f.append(Node(problem.initial))
    frontier_b.append(Node(problem.goal))

    while frontier_f and frontier_b:
        if frontier_f:
            node_f = frontier_f.pop()
            explored_f.add(node_f.state)
            if problem.goal_test(node_f.state) or node_f in frontier_b:
                while frontier_b:
                    node_b = frontier_b.pop()
                    if node_b == node_f:
                        # print('BUSQUEDA F', node_b, node_f)
                        sol = node_f.solution()
                        rev = list(reversed(node_b.solution()))
                        sol.extend(rev)
                        return len(sol) - 1, node_f.path_cost + node_b.path_cost, explored_f.union(explored_b), len(
                            frontier_f) + len(frontier_b)
                return len(node_f.solution()), node_f.path_cost, explored_f.union(explored_b), len(frontier_f) + len(
                    frontier_b)

            # search in explored nodes
            if node_f.state in explored_b:
                print('node_f IN EXPLORED B')

            # expand frontier
            frontier_f.extend(child for child in node_f.expand(problem)
                              if child.state not in explored_f and
                              child not in frontier_f)

        if frontier_b:
            node_b = frontier_b.pop()
            # print('B')
            explored_b.add(node_b.state)
            if node_b.state == problem.initial or node_b in frontier_f:
                while frontier_f:
                    node_f = frontier_f.pop()
                    if node_f == node_b:
                        # print('BUSQUEDA B', node_b, node_f)
                        sol = node_f.solution()
                        rev = list(reversed(node_b.solution()))
                        sol.extend(rev)
                        return len(sol) - 1, node_b.path_cost + node_f.path_cost, explored_b.union(explored_f), len(
                            frontier_b) + len(frontier_f)
                return len(node_b.solution()), node_b.path_cost, explored_b.union(explored_f), \
                       len(frontier_b) + len(frontier_f)

            # search in explored nodes
            if node_b.state in explored_f:
                print('node_f IN EXPLORED F')

            frontier_b.extend(child for child in node_b.expand(problem)
                              if child.state not in explored_b and
                              child not in frontier_b)

    return 0, 0, explored_f.union(explored_b), len(frontier_f) + len(frontier_b)
