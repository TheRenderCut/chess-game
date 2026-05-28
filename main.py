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
def print_board(board):
    for num,line in enumerate(board):
        print(f"{8-num} {' | '.join(line)}")
    print("  a   b   c   d   e   f   g   h")
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
    return False
def move_piece():
    move = input(("Enter Your Move (Ex. e2 e4): "))
    start, end = move.split()
    start_row = 8 - int(start[1])
    start_col = ord(start[0]) - ord('a')
    end_row = 8 - int(end[1])
    end_col = ord(end[0]) - ord('a')
    piece = board[start_row][start_col]
    if is_valid_pawn_move(piece,start_row,start_col,end_row,end_col):
        board[end_row][end_col] = piece
        board[start_row][start_col] = ' '
        print_board(board)
print_board(board)
move_piece()