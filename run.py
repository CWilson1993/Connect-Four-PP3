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


# The below prints the game board
def printBoard(board):
    rows = ['a','b','c','d','e','f']
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-'*(len(top)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(board[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(top)
    print('')

# The below code makes a random choice for the computer and prompts the player to make a move, giving parameters for the choice
def move(piece, board, Stacks, computer):
    Set0 = {'1','2','3','4','5','6','7'}
    if piece == computer:
        pos = randint(1,7)
        if len(Stacks[pos-1]) < 6:
            Stacks[pos-1].push(piece)
            board[6-len(Stacks[pos-1])][pos-1] = \
                Stacks[pos-1].peek()
        else:
            move(piece, board, Stacks, computer)
    else:
        pos = str(input('Your move: '))
        if (pos in Set0) == False:
            print('Input must be integer between 1 and 7')
            move(piece, board, Stacks, computer)
        else: 
            pos = int(pos)
            if len(Stacks[pos-1]) < 6:
                Stacks[pos-1].push(piece)
                board[6-len(Stacks[pos-1])][pos-1] = \
                    Stacks[pos-1].peek()
            else:
                print('Column full, try again...')
                move(piece, board, Stacks, computer)
    return board, Stacks