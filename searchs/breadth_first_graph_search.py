from peas.fifo_queue import FIFOQueue
from searchs.graph_search import graph_search


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())
