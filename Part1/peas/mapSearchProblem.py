from peas import mapClass

class MapSearchProblem():
    def __init__(self, initial, goal, mapPitts):
        """El constructor recibe  el estado inicial, el estado objetivo y un mapa (de clase Mapa)"""
        self.initial = initial
        self.goal = goal
        self.map = mapPitts

    def actions(self, state):
        """Retorna las acciones ejecutables desde ciudad state.
        El resultado es una lista de strings tipo 'goCity'. 
        Por ejemplo, en el mapa de Romania, las acciones desde Arad serian:
         ['goZerind', 'goTimisoara', 'goSibiu']"""
        neighbors = []
        acciones = []
        tupla = ()        
        neighbors = self.map.neighbors[state]
        for acc in range(len(neighbors)):
            acciones.append('go' + neighbors[acc][0])
        return acciones

    def result(self, state, action):
        """Retorna el estado que resulta de ejecutar la accion dada desde ciudad state.
        La accion debe ser alguna de self.actions(state)
        Por ejemplo, en el mapa de Romania, el resultado de aplicar la accion 'goZerind' 
        desde el estado 'Arad' seria 'Zerind'"""  
        newState = action[2]
        return newState
        
    def goal_test(self, state):
        return (self.goal == state) 

    def path_cost(self, c, state1, action, state2):
        """Retorna el costo del camino de state2 viniendo de state1 con la accion action 
        El costo del camino para llegar a state1 es c. El costo de la accion debe ser
        extraido de self.map."""
        actionCost = 0;
        destStates = self.map.neighbors[state1] #estado destino, state2
        for acc in range(len(destStates)):
            if (destStates[acc][0] == state2):
                actionCost = destStates[acc][1]
                break
        return c + actionCost;