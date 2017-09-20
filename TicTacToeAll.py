from random import randint
import copy, time
class TicTacToe:
    def __init__(self):
        self.count = 0
        self.uniqueCount = 0
    def copyBoard(self, board):
        return [board[0][:], board[1][:], board[2][:]]
    def isFull(self, board):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] is "N":
                    return False
        return True
    def hasWon(self, board):
        for r in range(len(board)):
            if board[r][0] is not "N":
                piece = board[r][0]
                if board[r][1] is piece and board[r][2] is piece:
                    return True
        for c in range(len(board)):
            if board[0][c] is not "N":
                piece = board[0][c]
                if board[1][c] is piece and board[2][c] is piece:
                    return True
        if board[0][0] is not "N":
            piece = board[0][0]
            if board[1][1] is piece and board[2][2] is piece:
                return True
        if board[2][0] is not "N":
            piece = board[2][0]
            if board[1][1] is piece and board[0][2] is piece:
                return True
        return False
    def placePiece(self, xTurn, r, c, board):
        newboard = self.copyBoard(board)
        if xTurn is True:
            newboard[r][c] = "X"
        else:
            newboard[r][c] = "O"
        return newboard
    def main(self, board, xTurn):
        if self.hasWon(board) or self.isFull(board):
            self.count += 1
            return
        for r in range(3):
            for c in range(3):
                if board[r][c] is not "N":
                    continue
                newboard = self.placePiece(xTurn, r, c, board)
                self.main(newboard, not xTurn)
                
b = TicTacToe()
t = time.time()
b.main([["N" for r in range(3)] for c in range(3)], True)
print time.time() - t
print b.count
