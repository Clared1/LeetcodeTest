from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.deque = deque(maxlen=k)
        self.k = k


    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True
        else:
            return False


    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.deque.popleft()
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.deque[0]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0



    def isFull(self) -> bool:
        return len(self.deque) == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()