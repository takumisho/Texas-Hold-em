from os import popen
import random


class PlayingCard:
    """definitio of Playing Card"""
#    SUIT_LIST = ('C', 'D', 'H', 'S')
    SUIT_LIST = ('♣', '♢', '♡', '♠')
    NUMBER_LIST = ('', 'A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'J', 'Q', 'K')

#   コンストラクタ
    def __init__(self, suit, number):
        """deconstructor of Playing Card"""
        self.suit = suit
        self.number = number

    def output(self):
        return self.suit + self.NUMBER_LIST[self.number]

#   特殊メソッドstr strを使用するときの振る舞い定義
    def __str__(self):
        return self.suit + self.NUMBER_LIST[self.number]

#   特殊メソッドeq == を使用するときの振る舞い定義
    def __eq__(self, other):
        return (self.suit == other.suit
                and self.number == other.number)

#   特殊メソッド hash関数を使用するときの振る舞い定義
#    def __hash__(self):
#        return hash((self.suit, self.number))

#   特殊メソッド >=    
    def __ge__(self):
        return self.val >= self.val

#   listクラスを継承 リストを使える
class Deck(list):
    """definitio of Deck"""
    def __init__(self):
        """deconstructor of Deck"""
#       基底クラス(list)のメソッドを呼び出す        
        super().__init__()
        self.extend([PlayingCard(x, y+1)
                     for x in PlayingCard.SUIT_LIST
                     for y in range(13)])
        self.shuffle()
        
#   基底クラスメソッドpopを呼び出す
    def pop(self):
        return super().pop()

    draw = pop

    def shuffle(self):
        """shuffle the deck"""
        random.shuffle(self)

#   特殊メソッド リストの要素を連結するstr
    def __str__(self):
        return " ".join([str(c).upper() for c in self])

#   ランダムな位置にカードを追加するinsert
    def insert(self, card):
        """insert the card at the random point"""
        i = random.randint(0, len(self))
        super().insert(i, card)


if __name__ == "__main__":
    card1 = PlayingCard(PlayingCard.SUIT_LIST[3], 1)
    card2 = PlayingCard(PlayingCard.SUIT_LIST[0], 11)
    card3 = PlayingCard(PlayingCard.SUIT_LIST[2], 12)
    card4 = PlayingCard(PlayingCard.SUIT_LIST[1], 13)
    print(card1, card2, card3, card4)

    deck = Deck()
    print(deck)
