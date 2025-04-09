class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        current_freq = self.freq.get(val, 0) + 1
        self.freq[val] = current_freq
        
        if current_freq > self.max_freq:
            self.max_freq = current_freq
        if current_freq not in self.group:
            self.group[current_freq] = []
        self.group[current_freq].append(val)

    def pop(self) -> int:
        most_freq_element = self.group[self.max_freq].pop()
        self.freq[most_freq_element] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return most_freq_element

# Example usage:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# print(obj.pop())  # Output: 5
# print(obj.pop())  # Output: 7
# print(obj.pop())  # Output: 5
# print(obj.pop())  # Output: 4
