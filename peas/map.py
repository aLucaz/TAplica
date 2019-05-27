from pandas import read_csv
from os import path


class Map:
    def __init__(self, neighbors, heuristics):
        self.neighbors = neighbors
        self.heuristics = heuristics


def create_map(edges_pitts_path, heuri_pitts_path=None):

    # Processing Pittsburgh data file
    data_map = read_csv(edges_pitts_path, ' ')
    pittsburgh_map = {}

    for i in range(len(data_map.nodeOne)):
        pittsburgh_map[str(data_map.nodeOne.iloc[i])] = []
        pittsburgh_map[str(data_map.nodeTwo.iloc[i])] = []
    
    for i in range(len(data_map.nodeOne)): 
        neighbors = (str(data_map.nodeTwo.iloc[i]), data_map.distance.iloc[i])
        pittsburgh_map[str(data_map.nodeOne.iloc[i])].append(neighbors)

        neighbors = (str(data_map.nodeOne.iloc[i]), data_map.distance.iloc[i])
        pittsburgh_map[str(data_map.nodeTwo.iloc[i])].append(neighbors)

    # Processing heuristics file
    pittsburgh_heu = {}
    if heuri_pitts_path is not None:  # no implica heuristica
        data_heu = read_csv(heuri_pitts_path, ' ')
        for i in range(len(data_heu.nodeStart)):
            pittsburgh_heu[str(data_heu.nodeStart.iloc[i])] = data_heu.distanceH.iloc[i]

    # Creating Map object with neighbors and heuristics from files
    pittsburgh_map = Map(pittsburgh_map, pittsburgh_heu)
    return pittsburgh_map
