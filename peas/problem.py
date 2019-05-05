
class Problem(object):
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def path_cost(self, path_cost, state1, action):
        raise NotImplementedError

    def value(self, state):
        raise NotImplementedError
