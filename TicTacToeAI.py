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

    if WhoseTurn == "AI":
        AITurnCount += 1
        AImove(WhoseTurn, Board, AITurnCount)
    if WhoseTurn == "PLAYER":
        PlayerMove(WhoseTurn, Board, AITurnCount)


def PlayerMove(WhoseTurn, Board, AITurnCount):
    choice = input("Enter a number 0-8: ")
    if choice.isdigit() == False:
        print ("Keep it an integer, buddy.")
        PlayerMove(WhoseTurn, Board, AITurnCount)
    if int(choice) > 8 or int(choice) < 0:
        print ("Make that a number between 0 and 8.")
        PlayerMove(WhoseTurn, Board, AITurnCount)
    if Board[int(choice)] == 'X' or Board[int(choice)] == 'O':
        print ("That's already taken! Try again.")
        PlayerMove(WhoseTurn, Board, AITurnCount)
    else:
        Board[int(choice)] = "O"
    WhoseTurn = "AI"
    WinnerCheck(WhoseTurn, Board, AITurnCount)



def AImove(WhoseTurn, Board, AITurnCount):
    alreadymoved = False
    Pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])



    if AITurnCount == 1:
        if Board[Random_Corner] != "O":
            Board[Random_Corner] = "X"



    else:
        for x in Pairs:
            if Board[x[0]] == "X" and Board[x[1]] == "X" and Board[x[2]] != "O":
                Board[x[2]] = "X"
                alreadymoved = True
                break
            if Board[x[1]] == "X" and Board[x[2]] == "X" and Board[x[0]] != "O":
                Board[x[0]] = "X"
                alreadymoved = True
                break
            if Board[x[0]] == "X" and Board[x[2]] == "X" and Board[x[1]] != "O":
                Board[x[1]] = "X"
                alreadymoved = True
                break
        for x in Pairs:
            if alreadymoved == False:
                if Board[x[0]] == "O" and Board[x[1]] == "O" and Board[x[2]] != "X":
                    Board[x[2]] = "X"
                    alreadymoved = True
                    break
                if Board[x[1]] == "O" and Board[x[2]] == "O" and Board[x[0]] != "X":
                    Board[x[0]] = "X"
                    alreadymoved = True
                    break
                if Board[x[0]] == "O" and Board[x[2]] == "O" and Board[x[1]] != "X":
                    Board[x[1]] = "X"
                    alreadymoved = True
                    break

    WhoseTurn = "PLAYER"
    WinnerCheck(WhoseTurn, Board, AITurnCount)



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
