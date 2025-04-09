from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def empty(self) -> bool:
        return not self.q1

# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())   # Output: 2
# print(obj.pop())   # Output: 2
# print(obj.empty()) # Output: False
