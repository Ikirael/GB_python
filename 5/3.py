
def print_board(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")

def win_check(board):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in win:
        if board[w[0]] == board[w[1]] == board[w[2]]:
            return 1

def error_check(board, turn):
    if board[turn-1] == 'x' or board[turn-1] == '0':
        print("Некорректный ход: на данной позиции ходили.")
        return 1
    elif turn < 1 or turn > 9:
        print("Неокрректный ход: данной позиции в игре не существует")
        return 1

def player_turn(board):
    i = 1
    while i <= 9:
        print_board(board)
        if i%2 == 1:
            a = int(input("Ход игрока 1: "))
            if error_check(board,a):
                i -=1
            else:
                board[a-1] = 'x'
        else:
            a = int(input("Ход игрока 2: "))
            if error_check(board,a):
                i -=1
            else:
                board[a-1] = '0'
        if win_check(board):
            print_board(board)
            if (i%2 == 1):
                print("Победа крестиков!!!")
            else:
                print("Победа ноликов!!!")
            return
        i+=1



board = []
for i in range(1,10):
    board.append(i)
player_turn(board)
