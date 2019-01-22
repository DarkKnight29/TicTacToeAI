__CreatedBy__ = 'Phani_Srikar'
import random
import sys




Pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])
Board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

WhoseTurn = "PLAYER"
AITurnCount = 0

Random_Corner = random.randint(1,5)


def printBoard(WhoseTurn, Board, AITurnCount):
    print (Board[0] + '{}'.format('|') + Board[1] + '{}'.format('|') + Board[2])
    print (Board[3] + '{}'.format('|') + Board[4] + '{}'.format('|') + Board[5])
    print (Board[6] + '{}'.format('|') + Board[7] + '{}'.format('|') + Board[8])

    print ("Turn: " + str(WhoseTurn))

    



printBoard(WhoseTurn, Board, AITurnCount)
