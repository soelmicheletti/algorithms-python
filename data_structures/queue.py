from collections import deque 
queue = deque([1, 2, 3]) 
queue.append(4) # O(1)
print(queue.popleft()) # returns 1, O(1) 