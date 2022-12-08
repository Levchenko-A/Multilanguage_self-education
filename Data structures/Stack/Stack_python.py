class Stack:
    ''' First In First Out'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


example = Stack()
example.print_stack()
print(example.is_empty())
example.push(1)
example.print_stack()
example.push(2)
example.push(3)
example.print_stack()
example.pop()
example.print_stack()
print(example.is_empty())
