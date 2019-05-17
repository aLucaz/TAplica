from flask import jsonify, request, Flask

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.breadth_first_graph_search import breadth_first_graph_search
from searchs.depth_graph_search import depth_graph_search

pitts_map = create_map()
app = Flask(__name__)


@app.route('/')
def main():
    return "TRABAJO DE APLICA"


@app.route('/route/graph/breadth', methods=['GET'])
def route_breadth_first():
    # get node id from url parameter
    node_id = request.args.get('id', default=104878620, type=int)

    # calculate efficient route with breadth first graph search
    pitts_problem = MapSearchProblem(str(node_id), '105012740', pitts_map)
    sol_node, visited_nodes = breadth_first_graph_search(pitts_problem)

    path, visited = sol_node.solution(), [node.state for node in visited_nodes]
    return jsonify(path=path, visited=visited)


@app.route('/route/graph/depth', methods=['GET'])
def route_depth_first():
    # get node id from url parameter
    node_id = request.args.get('id', default=104878620, type=int)

    # calculate efficient route with breadth first graph search
    pitts_problem = MapSearchProblem(str(node_id), '105012740', pitts_map)
    sol_node, visited_nodes = depth_graph_search(pitts_problem)

    path, visited = sol_node.solution(), [node.state for node in visited_nodes]
    return jsonify(path=path, visited=visited)
