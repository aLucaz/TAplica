from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.bidirectional_search import bidirectional_search


def test_bidirectional_search(pitts_problem):
    U , gF , gB , openF , openB , closedF , closedB= bidirectional_search(pitts_problem)
    print(U)
    #print(gF)
    #print(gB)
    print(closedF, "==============================>", closedB)
    #print(closedF)
    #print(closedB)
