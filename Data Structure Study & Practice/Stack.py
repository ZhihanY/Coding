class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peak(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)