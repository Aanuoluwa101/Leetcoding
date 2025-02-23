from collections import deque
from queue import Queue 
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
       self.queue.append(x)

       # rotate
       for _ in range(len(self.queue) - 1):
           self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    

stack = MyStack() 
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.top())
print(stack.empty())
print(stack.pop())
print(stack.empty())