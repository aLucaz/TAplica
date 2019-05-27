import click

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from test.test_astar_search import test_astar_search
from test.test_depth_graph_search import test_depth_graph_search
from test.test_breadth_first_graph_search import test_breadth_first_graph_search
from test.test_depth_limited_search import test_limited
from test.test_bidirectional_bfs_search import test_bidirectional_bfs_search


@click.command()
@click.option('-e', 'streets_filepath', required=True, type=click.Path(exists=True), help="archivo de segmentos de calles")
@click.option('-s', 'id_init', required=True, type=str, help="id de nodo inicial")
@click.option('-g', 'id_goal', required=True, type=str, help="id de nodo objetivo")
@click.option('-m', 'method', required=True, type=click.Choice(['bfs', 'dfs', 'ids', 'bis', 'astar']), help="método de búsqueda")
@click.option('-h', 'heuristic_filepath', type=click.Path(exists=True), help="archivo de información heurística")
def run(streets_filepath, id_init, id_goal, method, heuristic_filepath=None):
    # python main.py -e res/edges_pitts.txt -s 104878620 -g 105012740 -m bfs
    pitts_map = create_map(streets_filepath, heuristic_filepath)
    pitts_problem = MapSearchProblem(id_init, id_goal, pitts_map)
    if method == 'bfs':
        test_breadth_first_graph_search(pitts_problem)
    elif method == 'dfs':
        test_depth_graph_search(pitts_problem)
    elif method == 'ids':
        test_limited(pitts_problem)
    elif method == 'bis':
        test_bidirectional_bfs_search(pitts_problem)
    elif method == 'astar' and heuristic_filepath is not None:
        test_astar_search(pitts_problem)


def test():
    id_end = "105012740"
    pitts_map = create_map("res/edges_pitts.txt", "res/heuristics_pitts.txt")

    for id_start in ["104878620", "275754986", "656071251"]:
        print('=' * 150)
        pitts_problem = MapSearchProblem(id_start, id_end, pitts_map)
        test_breadth_first_graph_search(pitts_problem)
        test_depth_graph_search(pitts_problem)
        test_astar_search(pitts_problem)
        test_limited(pitts_problem)
        test_bidirectional_bfs_search(pitts_problem)


if __name__ == "__main__":
    run()
