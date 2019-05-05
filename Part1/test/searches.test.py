from matplotlib import pyplot as plt
import pandas as pd

from searchs import *

from peas import mapCreation as create 
from peas import mapClass as mc
from peas import mapSearchProblem as msp

from searchs import bestFirstGraphSearch as bfgs


if __name__ == "__main__":
    pittsMap = create.create_map()
    pittsProblem = msp.MapSearchProblem('104878620','105012740',pittsMap)
    solNode,exploredNodes = bfgs.astar_search(pittsProblem)
