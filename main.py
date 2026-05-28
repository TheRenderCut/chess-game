board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]
current_turn = "white"
def print_board(board):
    for num,line in enumerate(board):
        print(f"{8-num} {' | '.join(line)}")
    print("  a   b   c   d   e   f   g   h")
def change_turn():
    global current_turn
    if current_turn == "white":
        current_turn = "black"
    else:
        current_turn = "white"
def move_piece(piece,start_row,start_col,end_row,end_col):
    board[end_row][end_col] = piece
    board[start_row][start_col] = ' '
def is_valid_pawn_move(piece,start_row,start_col,end_row,end_col):
    if piece == 'P':
        starting_row = 6
        direction = -1
    else:
        starting_row = 1
        direction = 1
    if start_row == starting_row and end_row == start_row + 2*direction:
        if end_col == start_col:
            if board[start_row + direction][start_col] == ' ' and board[end_row][end_col] == ' ':
                return True
    elif end_col == start_col and end_row == start_row + direction:
        if board[end_row][end_col] == ' ':
            return True
    elif end_row == start_row + direction and abs(start_col - end_col) == 1:
        target = board[end_row][end_col]
        if target != ' ' and piece.isupper() != target.isupper():
            return True
    print("Invalid Move!")
    return False
def is_valid_rook_move(piece,start_row,start_col,end_row,end_col):
        if start_row == end_row and start_col == end_col:
            print("Invalid Move!")
            return False
        if start_col == end_col:
            step = 1 if end_row > start_row else -1
            for i in range(start_row + step, end_row, step):
                if board[i][start_col] != ' ':
                    print("Invalid Move!")
                    return False
            target = board[end_row][end_col]
            if target == ' ':
                return True
            elif piece.isupper() != target.isupper():
                return True
        elif start_row == end_row:
            step = 1 if end_col > start_col else -1
            for i in range(start_col + step, end_col, step):
                    if board[start_row][i] != ' ':
                        print("Invalid Move!")
                        return False
            target = board[end_row][end_col]
            if target == ' ':
                return True
            elif piece.isupper() != target.isupper():
                return True
        else:
            print("Invalid Move!")
            return False
def is_valid_bishop_move(piece,start_row,start_col,end_row,end_col):
    if start_row == end_row or start_col == end_col:
        print("Invalid Move!")
        return False
    if end_col > start_col:
        step_col = 1
    else:
        step_col = -1
    if end_row > start_row:
        step_row = 1
    else:
        step_row = -1
    if abs(start_row - end_row) == abs(start_col - end_col):
        current_row = start_row + step_row
        current_col = start_col + step_col
        while current_row != end_row and current_col != end_col:
            if board[current_row][current_col] != ' ':
                print("Invalid Move!")
                return False
            current_row += step_row
            current_col += step_col
        target = board[end_row][end_col]
        if target == ' ':
            return True
        if piece.isupper() != target.isupper():
            return True
    else:
        print("Invalid Move!")
        return False
def is_valid_knight_move(piece,start_row,start_col,end_row,end_col):
    row_diff = abs(start_row - end_row)
    col_diff = abs(start_col - end_col)
    if row_diff == 1 and col_diff == 2:
        target = board[end_row][end_col]
        if target == ' ':
            return True
        if piece.isupper() != target.isupper():
            return True
        else:
            print("Invalid Move!")
            return False
    elif row_diff == 2 and col_diff == 1:
        target = board[end_row][end_col]
        if target == ' ':
            return True
        if piece.isupper() != target.isupper():
            return True
        else:
            print("Invalid Move!")
            return False
    else:
        print("Invalid Move!")
        return False
def is_valid_queen_move(piece,start_row,start_col,end_row,end_col):
    if is_valid_bishop_move(piece,start_row,start_col,end_row,end_col) or is_valid_rook_move(piece,start_row,start_col,end_row,end_col):
        return True
    else:
        return False
def choose_piece():
    move = input(("Enter Your Move (Ex. e2 e4): "))
    start, end = move.split()
    start_row = 8 - int(start[1])
    start_col = ord(start[0]) - ord('a')
    end_row = 8 - int(end[1])
    end_col = ord(end[0]) - ord('a')
    piece = board[start_row][start_col]
    if piece == ' ':
        print("No Piece Selected")
        return
    if current_turn == "white" and piece.islower():
        print("Not your turn!")
        return
    if current_turn == "black" and piece.isupper():
        print("Not your turn!")
        return
    if piece.lower() == 'p':
        if is_valid_pawn_move(piece,start_row,start_col,end_row,end_col):
            move_piece(piece,start_row,start_col,end_row,end_col)
            change_turn()
    elif piece.lower() == 'r':
        if is_valid_rook_move(piece,start_row, start_col, end_row, end_col):
            move_piece(piece,start_row,start_col,end_row,end_col)
            change_turn()
    elif piece.lower() == 'b':
        if is_valid_bishop_move(piece,start_row, start_col, end_row, end_col):
            move_piece(piece,start_row,start_col,end_row,end_col)
            change_turn()
    elif piece.lower() == 'n':
        if is_valid_knight_move(piece,start_row, start_col, end_row, end_col):
            move_piece(piece,start_row,start_col,end_row,end_col)
            change_turn()
    elif piece.lower() == 'q':
        if is_valid_queen_move(piece,start_row, start_col, end_row, end_col):
            move_piece(piece,start_row,start_col,end_row,end_col)
            change_turn()
while True:
    print_board(board)
    choose_piece()