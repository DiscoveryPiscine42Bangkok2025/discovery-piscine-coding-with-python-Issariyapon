def checkmate(board):
    """
    Check if the King is in checkmate position
    """
    if not board or not board.strip():
        print("Fail")
        return
    
    lines = board.strip().split('\n')
    
    # Validate board (must be square)
    if not lines:
        print("Fail")
        return
    
    board_size = len(lines)
    for line in lines:
        if len(line) != board_size:
            print("Fail")
            return
    
    # Find the King position
    king_pos = None
    for i in range(board_size):
        for j in range(board_size):
            if lines[i][j] == 'K':
                if king_pos is not None:  # Multiple kings
                    print("Fail")
                    return
                king_pos = (i, j)
    
    if king_pos is None:  # No king found
        print("Fail")
        return
    
    king_row, king_col = king_pos
    
    # Check if King is under attack by any piece
    if is_under_attack(lines, king_row, king_col, board_size):
        print("Success")
    else:
        print("Fail")

def is_under_attack(board, king_row, king_col, size):
    """
    Check if the King at (king_row, king_col) is under attack
    """
    # Check for Pawn attacks
    if is_attacked_by_pawn(board, king_row, king_col, size):
        return True
    
    # Check for Rook attacks
    if is_attacked_by_rook(board, king_row, king_col, size):
        return True
    
    # Check for Bishop attacks
    if is_attacked_by_bishop(board, king_row, king_col, size):
        return True
    
    # Check for Queen attacks (combines Rook and Bishop)
    if is_attacked_by_queen(board, king_row, king_col, size):
        return True
    
    return False

def is_attacked_by_pawn(board, king_row, king_col, size):
    """
    Check if King is attacked by a Pawn
    Pawns attack diagonally upward (row - 1)
    """
    # Check diagonal positions where a pawn could attack the king
    pawn_positions = [
        (king_row + 1, king_col - 1),  # Bottom-left diagonal
        (king_row + 1, king_col + 1)   # Bottom-right diagonal
    ]
    
    for row, col in pawn_positions:
        if 0 <= row < size and 0 <= col < size:
            if board[row][col] == 'P':
                return True
    return False

def is_attacked_by_rook(board, king_row, king_col, size):
    """
    Check if King is attacked by a Rook
    Rooks attack horizontally and vertically
    """
    # Check horizontal and vertical directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            if piece == 'R':
                return True
            elif piece != '.' and piece != ' ':  # Hit another piece
                break
            row, col = row + dr, col + dc
    
    return False

def is_attacked_by_bishop(board, king_row, king_col, size):
    """
    Check if King is attacked by a Bishop
    Bishops attack diagonally
    """
    # Check diagonal directions
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # all diagonals
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            if piece == 'B':
                return True
            elif piece != '.' and piece != ' ':  # Hit another piece
                break
            row, col = row + dr, col + dc
    
    return False

def is_attacked_by_queen(board, king_row, king_col, size):
    """
    Check if King is attacked by a Queen
    Queens attack like both Rooks and Bishops
    """
    # Check all 8 directions (horizontal, vertical, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            if piece == 'Q':
                return True
            elif piece != '.' and piece != ' ':  # Hit another piece
                break
            row, col = row + dr, col + dc
    
    return False