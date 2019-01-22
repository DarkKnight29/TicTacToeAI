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


def WinnerCheck(WhoseTurn, Board, AITurnCount):
    for x in Pairs:
        win1 = Board[x[0]]
        win2 = Board[x[1]]
        win3 = Board[x[2]]
        if win1 == win2 and win2 == win3:
            if win1 == "X":
                print ("AI wins.")
                end()
            if win1 == "O":
                print ("Human wins. Did you cheat?")
                end()
        else:
            filledspaces = 0
            for i in range(8):
                if Board[i] != " " and Board[i] != "_":
                    filledspaces += 1
                if filledspaces == 8:
                    print ("A draw! You will never win!")
                    end()

    printBoard(WhoseTurn, Board, AITurnCount)

def end():
    print ("Here is the final Board.")
    print (Board[0] + '{}'.format('|') + Board[1] + '{}'.format('|') + Board[2])
    print (Board[3] + '{}'.format('|') + Board[4] + '{}'.format('|') + Board[5])
    print (Board[6] + '{}'.format('|') + Board[7] + '{}'.format('|') + Board[8])
    sys.exit(0)
