#定义棋子
EMPTY = 0
BLACK_SOLDIER = 1
WHITE_SOLDIER = 2
BLACK_KING = 3
WHITE_KING = 4

def init_board():
    board = [[EMPTY for _ in range(10)] for _ in range(10)]
    # C++版本 vector<vector<int>> board(10, vector<int>(10, 0));

    for row in range(10):
        for col in range(10):
            # 判断黑格条件 : row + col 是奇数即为黑格
            if (row + col) % 2 != 0:
                # 在黑格内摆放棋子
                if row < 4:
                    board[row][col] = BLACK_SOLDIER
                elif row > 5:
                    board[row][col] = WHITE_SOLDIER

    return board

def print_board(board):
    print("   " + " ".join([str(i) for i in range(10)]))
    print("   " + "-" * 21)

    for row in range(10):
        row_str = f"{row}|"
        for col in range(10):
            piece = board[row][col]

            #判断白格
            if (row + col) % 2 == 0:
                row_str += "  "
                continue

            if piece == EMPTY:
                row_str += ". "
            elif piece == BLACK_SOLDIER:
                row_str += "b "
            elif piece == WHITE_SOLDIER:
                row_str += "w "
            elif piece == BLACK_KING:
                row_str += "B "
            elif piece == WHITE_KING:
                row_str += "K "
            else:
                row_str += "? "

        print(row_str)
    print()

if __name__ == "__main__":
    b = init_board()
    print_board(b)