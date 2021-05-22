+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
<!-----solution----->

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queue=collections.deque()
def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    temp=[]
    while self.queue:
        temp.append(self.queue.popleft())
    self.queue.append(x)
    for item in temp:
        self.queue.append(item)
        
def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    return self.queue.popleft()

def top(self) -> int:
    """
    Get the top element.
    """
    return self.queue[0]

def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return len(self.queue)==0
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.a = []
    self.b = [] 

def push(self, x):
    self.a.append(x)
    
def pop(self):
    if len(self.b) != 0: 
        return self.b.pop()
    else:
        while len(self.a) != 0:
            self.b.append(self.a.pop())
        return self.b.pop()  

def peek(self):
    if len(self.b) != 0: 
        return self.b[-1]
    else:
        while len(self.a) != 0:
            self.b.append(self.a.pop())
        return self.b[-1]

def empty(self):
    return len(self.a) == 0 and len(self.b) == 0
```

## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    self.value=[]
    self.stackmin=[]
def push(self, x: int) -> None:  
    self.value.append(x)
    if self.stackmin and self.stackmin[-1]<x:
        self.stackmin.append(self.stackmin[-1])
    else:
        self.stackmin.append(x)
        
def pop(self) -> None:
    self.value.pop()
    self.stackmin.pop()
    
def top(self) -> int:
    return self.value[-1]

def getMin(self) -> int:
    return self.stackmin[-1]
```