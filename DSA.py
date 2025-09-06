# ⚠️ Queue

queue = []

# Enqueue

queue.append(1)
queue.append(2.0)
queue.append("Hello")
queue.append('A')

print(queue)

# Dequeue

popped1 = queue.pop(0)
popped2 = queue.pop(0)

print(popped1,'\n',popped2)

# Front

print(queue[0])

# Empty

print(len(queue) == 0)

''' Using Queue Library'''

from queue import Queue

q = Queue()

q.put(5)
q.put(2.0)
q.put("Hello")

print(q)

# Dequeue

popped = q.get()
popped1 = q.get()

print(popped, popped1)

# Front

print(q.queue[0])

# Empty
print(q.empty())

# Full

print(q.full())

'''We can also use
    ---from collections import dequeue
    to use queue operations, store and access them.'''