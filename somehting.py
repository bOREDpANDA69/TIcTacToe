import random

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

validInput = [[0,0], [0,1], [0,2],
              [1,0], [1,1], [1,2],
              [2,0], [2,1], [2,2],]

def printBoard():
    print("\033[2J\033[H")
    print('     A     B     C\n')
    for i in range(3):
        print(f' {i+1}   {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}\n')
    '''
    00   0A   0B   0C

    01   O  |  X  |  O

    02   X  |  O  |  X
    
    03   O  |  X  |  0
    '''
def hasWon():

    a,b = 'XXX','OOO'
    r,s = '',board[0][2]+board[1][1]+board[2][0]
    if s == a or s == b:
        return s[0]
    for i in range(3):
        p,q = '',''
        for j in range(3):
            p += board[j][i]
            q += board[i][j]

        if p == a or p == b:
            return p[0]
        if q == a or q == b:
            return q[0];
        r += board[i][i]
    
    if r == a or r == b:
        return r[0]

    return None;
    

def getMove(player):
    
    print(f' {player}\'s turn\n Your choice [ A/B/C 1/2/3 ]: ',end = '')
    x,y = input().split()
    return [int(y)-1,ord(x)-65] 

def getInfo():
    print(' [ X ] will be : ',end = '')
    p1 = input()
    print(' [ O ] will be : ',end = '')
    p2 = input()
    return [p1,p2]

def firstMove(playerList):

    print(' Who goes first?\n That will be randomly chosen.')
    r = random.randint(0,1)
    print(f' {playerList[r]} will go first!\n')
    return r

def main():

    printBoard()
    p = getInfo()
    f = firstMove(p)

    while True:

        move = getMove(p[f])
        while move not in validInput:
            print('Already used this move.')
            move = getMove(p[f])
        
        board[move[0]][move[1]] = 'X' if f == 0 else 'O'

        printBoard()

        if hasWon() != None:
            if hasWon() == 'X':
                print(f' Congratulations {p[0]} has won the game!!')
            else:
                print(f' Congratulations {p[1]} has won the game!!')
            break

        validInput.remove(move)

        if validInput == []:
            print("Looks like it's a tough match, DRAW !")
            break

        f = 0 if f == 1 else 1

main()
