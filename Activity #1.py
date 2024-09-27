class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("top from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def len(self):
        return len(self.items)

def simulate_stack_operations():
    stack = Stack()

    stack.push(5)
    stack.push(3)
    print(stack.len())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())
    stack.push(7)
    stack.push(9)
    print(stack.top())
    stack.push(4)
    print(stack.len())
    print(stack.pop())
    stack.push(6)
    stack.push(8)
    print(stack.pop())

def simulate_final_operations():
    stack = Stack()
    pop_results = []

    stack.push(5)
    stack.push(3)
    pop_results.append(stack.pop())
    stack.push(2)
    stack.push(8)
    pop_results.append(stack.pop())
    pop_results.append(stack.pop())
    stack.push(9)
    stack.push(1)
    pop_results.append(stack.pop())
    stack.push(7)
    stack.push(6)
    pop_results.append(stack.pop())
    pop_results.append(stack.pop())
    stack.push(4)
    pop_results.append(stack.pop())
    pop_results.append(stack.pop())

    print(pop_results)

print("Table:")
simulate_stack_operations()
print()
print("Values are returned during the following series of stack operation")
simulate_final_operations()
