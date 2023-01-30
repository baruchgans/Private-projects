class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.items = [None] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value

        # Check if it is the first time
        if self.front == -1:
            self.front = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.items[self.front] = None
        # Check if it will be empty now
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
