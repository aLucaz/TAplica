from matplotlib import pyplot as plt
import pandas as pd


def create_map():
    data = pd.read_csv('./res/edges_pitts.txt',' ')
    pittsburgh = {}

    for i in range(len(data.nodeOne)):
        pittsburgh[str(data.nodeOne.iloc[i])] = []
        pittsburgh[str(data.nodeTwo.iloc[i])] = []
    
    for i in range(len(data.nodeOne)): 
        neighbors = (str(data.nodeTwo.iloc[i]),data.distance.iloc[i])
        pittsburgh[str(data.nodeOne.iloc[i])].append(neighbors) 
        neighbors = (str(data.nodeOne.iloc[i]),data.distance.iloc[i])
        pittsburgh[str(data.nodeTwo.iloc[i])].append(neighbors)

    return pittsburgh


if __name__ == "__main__":
    pittsburghMap = create_map()
    cont = 0
    for nodo,neigh in pittsburghMap.items(): 
        print(cont," ",nodo,"=>",neigh)
        cont += 1