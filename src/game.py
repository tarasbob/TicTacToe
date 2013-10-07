import random

def whoWins(pos):
    for i in range(3):
        if pos[i][0] == pos[i][1] == pos[i][2] and pos[i][0] != ' ':
            return pos[i][0]

    for i in range(3):
        if pos[0][i] == pos[1][i] == pos[2][i] and pos[0][i] != ' ':
            return pos[0][i]

    if pos[0][0] == pos[1][1] == pos[2][2] and pos[0][0] != ' ':
        return pos[0][0]

    if pos[0][2] == pos[1][1] == pos[2][0] and pos[0][2] != ' ':
        return pos[0][2]

    if len(legalMoves(pos)) == 0:
        return 't'
    
    return 'u'

def getNewPos(pos, move):
    y, x = move
    
    tlist[y, x]
            
def printPos(pos):
    print("------")
    for i in range(3):
        print (pos[i])

def legalMoves(pos):
    moves = []
    for i in range(3):
        for j in range(3):
            if pos[i][j] == ' ':
                moves.append((i, j))
    return moves

def updatePos(pos, turn, move):
    lpos = [list(pos[x]) for x in range(3)]
    lpos[move[0]][move[1]] = turn
    npos = tuple([tuple(k) for k in lpos])
    turn = 'w' if turn == 'b' else 'b'
    return npos, turn

def simulate(pos, turn):
    #printPos(pos)
    winner = whoWins(pos)
    if winner == 'u':
        m = random.choice(legalMoves(pos))
        npos, turn = updatePos(pos, turn, m)
        return simulate(npos, turn)
    else:
        return winner
        

def bestMove(pos, turn):
    numSim = 100000
    moves = legalMoves(pos)
    scores = dict()
    for move in moves:
        scores[move] = 0
        npos, nturn = updatePos(pos, turn, move)
        for i in range(numSim):
            winner = simulate(npos, nturn)
            if winner == turn:
                scores[move] += 1
            elif winner == 't':
                scores[move] += 1
                
    bestmove = ''
    bestscore = 0
    print(scores)
    for key in scores:
        if scores[key] > bestscore:
            bestmove = key
            bestscore = scores[key]
    return bestmove
        
def playGame():
    turn = 'b'
    pos = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '))

    while whoWins(pos) == 'u':
        printPos(pos)
        if turn == 'b':
            userMove = tuple([int(i) for i in input('Enter Move ').split()])
            pos, turn = updatePos(pos, turn, userMove)
        else:
            compMove = bestMove(pos, turn)
            pos, turn = updatePos(pos, turn, compMove)
    print ("winner: ", whoWins(pos))
    
startPos = ((' ', ' ', 'w'), (' ', 'b', ' '), (' ', ' ', ' '))
playGame()

        
