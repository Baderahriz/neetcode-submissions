class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("INF")
        self.minValues = []

    def push(self, val: int) -> None:
        if val <= self.min:
            self.min = val
        self.stack.insert(0, val)
        self.minValues.insert(0, self.min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(0)
            self.minValues.pop(0)
            if len(self.minValues) > 1:
                self.min = self.minValues[0]
            else:
                self.min = float("INF")

    def top(self) -> int:
        if self.stack:
            return self.stack[0]

    def getMin(self) -> int:
        if self.minValues:
            return self.minValues[0]
