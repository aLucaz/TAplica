from collections import deque
# Breadth First Search


class FIFOQueue(deque):
    def pop(self):
        return self.popleft()

    def isEmpty(self):
        return len(self) == 0
