from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.bidirectional_search import bidirectional_search


def test_bidirectional_search(pitts_problem):
    U , gF , gB , openF , openB , closedF , closedB, numB= bidirectional_search(pitts_problem)
    print("U", U)
    print("gF: ", gF)
    print("gB:" , gB)
    
    print(closedF, "==============================>", closedB)
    print(openF,"===",openB)
    
    print("numero de bucles :", numB)
    #print(closedF)
    #print(closedB)
    #print("ESTO ES LO QUE QUIERO >:v")
    print(len(openF)+len(openB)+len(closedF)+len(closedB))
    print(len(gF)+len(gB))
    #print(len(closedB)+len(closedF))
