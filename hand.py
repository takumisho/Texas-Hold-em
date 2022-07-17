#モジュールのインポート
from pcard import *

class Hand(Deck):
    """手札の定義"""
    def __init__(self):
        self.myhand = random.sample(Deck(),k=7)
        super().__init__()
        self.clear()
    def __str__(self):
        string = [str(c).split() for c in self.myhand]
        self.myhand = " ".join(" ".join(l) for l in string)
        return  self.myhand
    def spli(self):
        string = str(self).split()
        return string

    def sort(self):
        super().sort(key=lambda x: (x.number, x.suit))
