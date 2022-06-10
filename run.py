# Class stack (for each column)
class Stack:
    def __init__(self):
        self._list = []
    
    def __len__(self):
        return len(self._list)    
    
    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return
    
    def peek(self):
        return self._list[-1]


# Below is the code to initilaize the board which will be empty at first
def initialBoard():
    rows = ['a','b','c','d','e','f']
    board = []
    for i in range(0,len(rows)):
        board.append([' '] * 7)
    
    return board


# Below is the empty initial stacks, the board will require 7 stacks(columns) to play connect four
def initStacks():
    S = [ Stack(), Stack(), Stack(), 
         Stack(), Stack(), Stack(), Stack() ]
    return S

