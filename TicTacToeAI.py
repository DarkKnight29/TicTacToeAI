__CreatedBy__ = 'Phani_Srikar'
import random
import sys




pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])
corners = [0, 2, 6, 8]
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

turn = "PLAYER"
aiturn = 0

Random_Corner = random.randint(1,5)


def printboard(turn, board, aiturn):
    print (board[0] + '{}'.format('|') + board[1] + '{}'.format('|') + board[2])
    print (board[3] + '{}'.format('|') + board[4] + '{}'.format('|') + board[5])
    print (board[6] + '{}'.format('|') + board[7] + '{}'.format('|') + board[8])

    print ("Turn: " + str(turn))

    if turn == "AI":
        aiturn += 1
        aimove(turn, board, aiturn)
    if turn == "PLAYER":
        playermove(turn, board, aiturn)



def playermove(turn, board, aiturn):
    choice = input("Enter a number 0-8: ")
    if choice.isdigit() == False:
        print ("Keep it an integer, buddy.")
        playermove(turn, board, aiturn)
    if int(choice) > 8 or int(choice) < 0:
        print ("Make that a number between 0 and 8.")
        playermove(turn, board, aiturn)
    if board[int(choice)] == 'X' or board[int(choice)] == 'O':
        print ("That's already taken! Try again.")
        playermove(turn, board, aiturn)
    else:
        board[int(choice)] = "O"
    turn = "AI"
    checkforwin(turn, board, aiturn)



def aimove(turn, board, aiturn):
    alreadymoved = False
    completes = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])



    if aiturn == 1:
        if board[Random_Corner] != "O":
            board[Random_Corner] = "X"



    else:
        for x in completes:
            if board[x[0]] == "X" and board[x[1]] == "X" and board[x[2]] != "O":
                board[x[2]] = "X"
                alreadymoved = True
                break
            if board[x[1]] == "X" and board[x[2]] == "X" and board[x[0]] != "O":
                board[x[0]] = "X"
                alreadymoved = True
                break
            if board[x[0]] == "X" and board[x[2]] == "X" and board[x[1]] != "O":
                board[x[1]] = "X"
                alreadymoved = True
                break
        for x in completes:
            if alreadymoved == False:
                if board[x[0]] == "O" and board[x[1]] == "O" and board[x[2]] != "X":
                    board[x[2]] = "X"
                    alreadymoved = True
                    break
                if board[x[1]] == "O" and board[x[2]] == "O" and board[x[0]] != "X":
                    board[x[0]] = "X"
                    alreadymoved = True
                    break
                if board[x[0]] == "O" and board[x[2]] == "O" and board[x[1]] != "X":
                    board[x[1]] = "X"
                    alreadymoved = True
                    break

    turn = "PLAYER"
    checkforwin(turn, board, aiturn)


def checkforwin(turn, board, aiturn):
    for x in pairs:
        win1 = board[x[0]]
        win2 = board[x[1]]
        win3 = board[x[2]]
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
                if board[i] != " " and board[i] != "_":
                    filledspaces += 1
                if filledspaces == 8:
                    print ("A draw! You will never win!")
                    end()

    printboard(turn, board, aiturn)

def end():
    print ("Here is the final board.")
    print (board[0] + '{}'.format('|') + board[1] + '{}'.format('|') + board[2])
    print (board[3] + '{}'.format('|') + board[4] + '{}'.format('|') + board[5])
    print (board[6] + '{}'.format('|') + board[7] + '{}'.format('|') + board[8])
    sys.exit(0)


printboard(turn, board, aiturn)
