class ChessBoard:
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self):
        pass


class ChessSquare:
    def __init__(self, letter, number, color, left, right, top, bottom, is_vacant):
        self.letter = letter
        self.number = number
        self.color = color
        self.left = left
        self.right = right
        self.top = top
        self.botton = bottom
        self.is_vacant = is_vacant


class ChessFigure:
    pass
