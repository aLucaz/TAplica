from peas.problem import Problem


class MapSearchProblem(Problem):

    def value(self, state):
        pass

    def __init__(self, initial, goal, map_pitts):
        """ El constructor recibe  el estado inicial, el estado
            objetivo y un mapa (de clase Mapa) """
        super().__init__(initial, goal)
        self.map = map_pitts

    def actions(self, state):
        """ Retorna las acciones ejecutables desde ciudad state.
            El resultado es una lista de strings tipo 'goCity'. """
        acciones = []
        neighbors = self.map.neighbors[state]
        for i in range(len(neighbors)):
            acciones.append(neighbors[i][0])
        return acciones

    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, path_cost, state1, action):
        """Retorna el costo del camino de state2 viniendo de state1 con la acción action 
        El costo del camino para llegar a state1 es c. El costo de la acción debe ser
        extraído de self.map."""
        state2 = action  # TODO(3): en serio, pensar en una buna implementacion

        action_cost = 0
        destinations = self.map.neighbors[state1]  # estado destino, state2
        
        for i in range(len(destinations)):
            if destinations[i][0] == state2:
                action_cost = destinations[i][1]
                break

        return path_cost + action_cost
