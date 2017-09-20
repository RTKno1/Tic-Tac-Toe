from random import randint
class TicTacToe:
    def __init__(self):
        self.board = [["N" for r in range(3)] for c in range(3)]
    def placePosition(self, r, c):
        self.board[r][c] = "X"
    def display(self):
        p = ""
        for r in range(len(self.board)):
            p += "\n"
            p += "--------"
            p += "\n" + "|"
            for c in range(len(self.board)):
                p += str(self.board[r][c]) + "|" 
        print p
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
                    return True
        for c in range(len(self.board)):
            if self.board[r][0] is not "N":
                piece = self.board[0][c]
                if self.board[1][c] is piece and self.board[2][c] is piece:
                    return True
        if self.board[0][0] is not "N":
            piece = self.board[0][0]
            if self.board[1][1] is piece and self.board[2][2] is piece:
                return True
        if self.board[2][0] is not "N":
            piece = self.board[2][0]
            if self.board[1][1] is piece and self.board[0][2] is piece:
                return True
        return False
    def placePiece(self):
        r = randint(0, 2)
        c = randint(0, 2)
        while self.board[r][c] is not "N":
            r = randint(0, 2)
            c = randint(0, 2)
        self.board[r][c] = "O"
        self.display()
    def main(self):
        position = raw_input("Would you like to go first or second? type F for first and S for second. ")
        print position
        if position == 'S' or position == 's':
            self.placePiece()
        while self.isFull() is False:
            row = input("Where would you like to place? Insert row. ")
            col = input("Where would you like to place? Insert col. ")
            self.placePosition(row, col)
            self.display()
            if self.hasWon():
                print "You Win!"
                break
            self.placePiece()
            if self.hasWon():
                print "You Lose!"
                break
b = TicTacToe()
b.main()
