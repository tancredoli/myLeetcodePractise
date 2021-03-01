from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.max = 0

    def push(self, x: int) -> None:
        temp = self.freq[x] + 1
        self.freq[x] = temp
        if temp > self.max:
            self.max = temp
        self.group[temp].append(x)

    def pop(self) -> int:
        curr = self.group[self.max].pop()
        self.freq[curr] -= 1
        if not self.group[self.max]:
            self.max -= 1

        return curr