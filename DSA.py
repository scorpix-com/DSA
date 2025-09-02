#  ⚠️ Stack using List

def push(data):
    stack.append(data)

def _pop():
    return stack.pop()

def top():
    return stack[-1]

def search(data):
    for val in stack: 
        if val == data: return "Found"
        else: return "Not Found"

stack = [1,2,3]

print(stack)
print("Pushing: 5", push(5))
print("Pushing: 7", push(7))
print(stack)
print("Popping: ", _pop())
print(stack)
print("Top: ", top())
print("Search: 5", search(5))


# Stack using Deque

from collections import deque

stack = deque([4,5,6])

print("---Using deque")

print(f"Push: 8 {push(8)}")
print(f"Push: 9 {push(9)}")
print(stack)
print(f"Pop:  {_pop()}")
print(f"Top:  {top()}")
print(f"Search:  {search(10)}")
