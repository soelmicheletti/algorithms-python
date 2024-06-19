stack = []
for i in range(10):
    stack.append(i) # O(1)
stack.pop() # O(1)
top = stack[:-1] # O(1)