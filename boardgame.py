
board = {1: 'NULL', 2: 'NULL', 3: 'NULL', 4: 'NULL', 5: 'NULL', 6: 'NULL', 7: 'NULL', 8: 'NULL', 9: 'NULL'}
class card:
    def __init__(self, location, owner, element):
        self.location = str(location)
        self.owner = str(owner)
        self.element = str(element)
        print('Card created\n')       
    def __str__(self):
        return f"{self.location}, {self.owner}, {self.element}"

for object in board:
    board[object] = card(object, "NONE", "NULL")


def check():
    for object in board:
        if board[object].element == 'WATER' and board[object + 1].element == 'FIRE':
            board[object].element = 'NULL'
            board[object + 1].element = 'NULL'
            print('Water extinguished fire')

def Board():
    for object in board:
        print(f"{board[object].__str__()}\n")

action = ''
while action.upper() != 'END':
    action = input('Enter action: \n')
    if action.upper() == 'PLACE':
        square = int(input('Which square? \n'))
        change = input('What element? \n')
        board[square].element = change.upper()
        board[int(square)].owner = 'PLAYER'        
        print(board[square].__str__())
    if action.upper() == 'BOARD':
        Board()
    check()