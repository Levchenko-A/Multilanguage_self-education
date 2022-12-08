class Queue:
    ''' First In Last Out'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_to_queue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)


example = Queue()
example.print_queue()
print(example.is_empty())
example.add_to_queue(1)
example.print_queue()
example.add_to_queue(2)
example.add_to_queue(3)
example.print_queue()
example.dequeue()
example.print_queue()
print(example.is_empty())
