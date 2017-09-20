from random import randint
class TicTacToe:
    def __init__(self):
        self.board = [["N" for r in range(3)] for c in range(3)]
    def display(self):
        p = ""
        for r in range(len(self.board)):
            p += "\n"
            p += "--------"
            p += "\n" + "|"
            for c in range(len(self.board)):
                p += str(self.board[r][c]) + "|" 
        print p
    def placePosition(self, board, t, player):
        r = t[0]
        c = t[1]
        if player is True:
            board[r][c] = "X"
        else:
            board[r][c] = "O"
        return board
    def freeSpace(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] is "N":
                    moves.append((r, c))
        return moves
    def isFull(self):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] is "N":
                    return False
        return True
    def hasWon(self):
        for r in range(len(self.board)):
            if self.board[r][0] is not "N":
                piece = self.board[r][0]
                if self.board[r][1] is piece and self.board[r][2] is piece:
                    return piece
        for c in range(len(self.board)):
            if self.board[r][0] is not "N":
                piece = self.board[0][c]
                if self.board[1][c] is piece and self.board[2][c] is piece:
                    return piece
        if self.board[0][0] is not "N":
            piece = self.board[0][0]
            if self.board[1][1] is piece and self.board[2][2] is piece:
                return piece
        if self.board[2][0] is not "N":
            piece = self.board[2][0]
            if self.board[1][1] is piece and self.board[0][2] is piece:
                return piece
        return False
    def bestLocation(self, board, xTurn):
        if self.hasWon() is "X":
            return -1
        elif self.hasWon() is "O":
            return 1
        elif self.isFull():
            return 0
        for moves in self.freeSpace():
            newboard = self.placePosition(board, moves, xTurn)
            val = self.bestLocation(newboard, not xTurn)
        #finish
            
    def main(self):
        position = raw_input("Would you like to go first or second? type F for first and S for second. ")
        if position == 'S' or position == 's':
            self.board = self.placePosition(self.board, self.bestLocation(self.board, False), False)
        while self.isFull() is False:
            row = input("Where would you like to place? Insert row. ")
            col = input("Where would you like to place? Insert col. ")
            self.board = self.placePosition(self.board, (row, col), True)
            self.display()
            if self.hasWon() is "X":
                print "You Win!"
                break
            self.placePosition(self.board, self.bestLocation(self.board, False), False)
            if self.hasWon() is "O":
                print "You Lose!"
                break
        print "Its a tie!"
b = TicTacToe()
b.main()
