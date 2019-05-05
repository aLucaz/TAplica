import bisect

class Frontier:
    """ Constructor de la frontera de prioridad, le paso la funcion de evaluacion """
    def __init__(self, fn):
        self.prioq = []
        self.fn = fn

    """ Agrego un nodo en la posicion correcta de acuerdo a su funcion de evaluacion, menor distancia a mayor 
    distancia """
    def add(self, node):
        fn = self.fn(node)
        bisect.insort(self.prioq, (fn, node))

    """ Remuevo el primero elemento de la priorityQ """
    def pop(self):
        (fn, node) = self.prioq.pop(0)
        return node

    """ Reemplazo el nodo que tengo en mi lista con el nodo que pasa como parámetro """
    def replace(self, node):
        for (i, (fn, old_node)) in enumerate(self.prioq):
            if old_node.state == node.state:
                self.prioq[i] = (self.fn(node), node)
                return

    """ Para saber si algún nodo esta en la frontera """
    def __contains__(self, node):
        return any(item[1].state == node.state for item in self.prioq)
        
    """ Para obtener el valor de la funcion de evaluacion de un nodo de la frontera"""
    def __getitem__(self, node):
        for fn, nodei in self.prioq:
            if nodei.state == node.state:
                return fn
