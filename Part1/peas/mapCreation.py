import pandas as pd

from peas import mapClass as mc

def create_map():
    dataMap = pd.read_csv('./res/edges_pitts.txt',' ')
    pittsburgh_M = {}

    for i in range(len(dataMap.nodeOne)):
        pittsburgh_M[str(dataMap.nodeOne.iloc[i])] = []
        pittsburgh_M[str(dataMap.nodeTwo.iloc[i])] = []
    
    for i in range(len(dataMap.nodeOne)): 
        neighbors = (str(dataMap.nodeTwo.iloc[i]),dataMap.distance.iloc[i])
        pittsburgh_M[str(dataMap.nodeOne.iloc[i])].append(neighbors) 
        neighbors = (str(dataMap.nodeOne.iloc[i]),dataMap.distance.iloc[i])
        pittsburgh_M[str(dataMap.nodeTwo.iloc[i])].append(neighbors)

    dataHeu = pd.read_csv('./res/heuristics_pitts.txt',' ')
    pittsburgh_H = {}

    for i in range(len(dataHeu.nodeStart)):
        pittsburgh_H[str(dataHeu.nodeStart.iloc[i])] = dataHeu.distanceH.iloc[i]

    pittsburgh_Map = mc.Map(pittsburgh_M,pittsburgh_H)
    return pittsburgh_Map