from searchs.bidirectional_bfs_search import bidirectional_search


def test_bidirectional_bfs_search(problem):
    n_route, cost, visited_nodes, n_frontier = bidirectional_search(problem)

    print("Costo de la ruta encontrada: {} Km".format(cost))
    print("Número de nodos en la ruta encontrada: {}".format(n_route))
    print("Número de nodos visitados: {}".format(len(visited_nodes)))
    print("Número de nodos en memoria: {}".format(len(visited_nodes) + n_frontier))
