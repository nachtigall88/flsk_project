class ChessBoard:
    """клас для створення шахівниці"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self):
        pass


class ChessSquare:
    """
    клас для створення клітини шахівниці, опису її властивостей
    """
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
    """
    клас для створення шахових фігур
    """
    def __init__(self, color, step):
        self.color = color
        self.step = step

class Player:
    """
    клас для створення одного із вдох гравців
    """
    pass