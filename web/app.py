from flask import jsonify, request, Flask, render_template

from peas.map import create_map
from peas.map_search_problem import MapSearchProblem

from searchs.depth_limited_search import iterative_deepening_search
from searchs.breadth_first_graph_search import breadth_first_graph_search
from searchs.depth_graph_search import depth_graph_search

pitts_map = create_map()
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/route/graph/breadth', methods=['GET'])
def route_breadth_first():
    # get node id from url parameter
    node_id = request.args.get('id', default=104878620, type=int)

    # calculate efficient route with breadth first graph search
    pitts_problem = MapSearchProblem(str(node_id), '105012740', pitts_map)
    sol_node, explored, cant = breadth_first_graph_search(pitts_problem)

    path, explored = sol_node.solution(), list(explored)
    return jsonify(path=path, explored=explored)


@app.route('/route/graph/depth', methods=['GET'])
def route_depth_first():
    # get node id from url parameter
    node_id = request.args.get('id', default=104878620, type=int)

    # calculate efficient route with breadth first graph search
    pitts_problem = MapSearchProblem(str(node_id), '105012740', pitts_map)
    sol_node, explored, cant = depth_graph_search(pitts_problem)

    path, explored = sol_node.solution(), list(explored)
    return jsonify(path=path, explored=explored)


@app.route('/route/graph/iterative', methods=['GET'])
def route_iterative_deepening():
    # get node id from url parameter
    node_id = request.args.get('id', default=104878620, type=int)

    # calculate efficient route with breadth first graph search
    pitts_problem = MapSearchProblem(str(node_id), '105012740', pitts_map)
    sol_node, explored = iterative_deepening_search(pitts_problem)

    path, explored = sol_node.solution(), list(explored)
    return jsonify(path=path, explored=explored)

