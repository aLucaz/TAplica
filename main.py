import click

from test.test_depth_graph_search import test_depth_graph_search
from test.test_searches import test_breadth
from test.test_breadth_first_graph_search import test_breadth_first_graph_search


@click.command()
@click.option('-e', required=True, type=click.File('r'), help="archivo de segmentos de calles")
@click.option('-s', required=True, type=int, help="id de nodo inicial")
@click.option('-g', required=True, type=int, help="id de nodo objetivo")
@click.option('-m', required=True, type=click.Choice(['bfs','dfs','ids','bis','astar']), help="método de búsqueda")
@click.option('-h', type=click.File('r'), help="archivo de información heurística")
def run(streets_file, id_init, id_goal, method, heuristic_file):
    # print("streets file  : ", streets_file)
    print("node id init  : ", id_init)
    print("node id goal  : ", id_goal)
    print("search method : ", method)
    # print("heuristic file: ", heuristic_file)


if __name__ == "__main__":
    # run()
    # test_breadth_first_graph_search()
    test_depth_graph_search()
