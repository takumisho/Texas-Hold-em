from pcard import *
from hand import Hand
import collections

A_straight = [1, 10, 11, 12, 13]
number = [0,0]

#自分が入力したものを判定したい場合
"""def set_up(self):
    '''poker hand parser'''
    self.clear()
    string = input("マーク、数字の組を7つ入力してください\n")
    if type(string) == Hand:
        for card in string.spli():        
            try:
                self.append(PlayingCard(card[0], int(card[1:])))#数字が二桁の時はcard[1]にするとおかしくなる
            #数字がA、Kなどと書かれていたとき用
            except ValueError:
                self.append(PlayingCard(
                    card[0], PlayingCard.NUMBER_LIST.index(card[1:])))
            except:
                raise
    elif type(string) == str:
        for card in string.split():        
            try:
                self.append(PlayingCard(card[0], int(card[1:])))#数字が二桁の時はcard[1]にするとおかしくなる
            #数字がA、Kなどと書かれていたとき用
            except ValueError:
                self.append(PlayingCard(
                    card[0], PlayingCard.NUMBER_LIST.index(card[1:])))
            except:
                raise        
Hand.set_up = set_up"""

def set_up(self, string):
    '''poker hand parser'''
    self.clear()
#   手札をhand.py等を用いて作った場合 クラス:Hand    
    if type(string) == Hand:
        for card in string.spli():        
            try:
                self.append(PlayingCard(card[0], int(card[1:])))#数字が二桁の時はcard[1]にするとおかしくなる
            #数字がA、Kなどと書かれていたとき用
            except ValueError:
                self.append(PlayingCard(
                    card[0], PlayingCard.NUMBER_LIST.index(card[1:])))
            except:
                raise
#   "♣2 ♢12 ♣1 ♣10 ♣9 d5 h7" のように直接プログラムに打ち込んだ手札の場合 クラス:str            
    elif type(string) == str:
        for card in string.split():        
            try:
                self.append(PlayingCard(card[0], int(card[1:])))#数字が二桁の時はcard[1]にするとおかしくなる
            #数字がA、Kなどと書かれていたとき用
            except ValueError:
                self.append(PlayingCard(
                    card[0], PlayingCard.NUMBER_LIST.index(card[1:])))
            except:
                raise        
Hand.set_up = set_up

"""以下は役の判定方法"""
#ロイヤルストレートフラッシュ
def is_royal_straight_flush(self):
    if self.is_straight() and self.is_flush() and set(A_straight) <= set([self[i].number for i in range(7)]):
        number[0] = 1
        return True
    else:
        return False
Hand.is_royal_straight_flush = is_royal_straight_flush                 

#フォーカード
def is_four_of_a_kind(self):
    self.sort()
    if ( self[0].number == self[3].number or self[1].number == self[4].number
    or self[2].number == self[5].number or self[3].number == self[6].number):
        number[0] = self[3].number
        return True
    else:
        return False

Hand.is_four_of_a_kind = is_four_of_a_kind

#ストレートフラッシュ
def is_straight_flush(self):
    if self.is_straight() and self.is_flush():
        self.is_straight()
        return True
    else:
        return False
setattr(Hand, "is_straight_flush", is_straight_flush)

#フルハウス
def is_full_house(self):
    self.sort()
    num = collections.Counter([self[i].number for i in range(7)])
    value = num.most_common()
    if value[0][1] == 3 and value[1][1] == 2:
        number[0] = value[0][0]
        number[1] = value[1][0]
        return True
    elif value[0][1] == 3 and value[1][1] == 3:
        number[0] = max(value[0][0],value[1][0])
        number[1] = min(value[0][0],value[1][0])
        if number[1] == 1:
            number[1] = number[0]
            number[0] = 1
        return True
    else:
        return False
Hand.is_full_house = is_full_house

#フラッシュ
def is_flush(self):
#   マークの出現回数を辞書型出力 keyに要素 値に出現回数 {'s' : 3,'h' : 2}的な
    num = collections.Counter([self[i].suit for i in range(7)])
#   出現回数の多い順に並び替えたリストを作る (要素, 出現回数)という形のタプルが要素  
    value = num.most_common()
    if value[0][1] >= 5:
        self.sort()
        if self[0].number == 1 and self[0].suit == value[0][0]:
            number[0] = 1
            return True
        for i in range(0,3):
            if self[6-i].suit == value[0][0]:
                number[0] =self[6-i].number 
                break
        return True
    else:
        return False
Hand.is_flush = is_flush

#ストレート
def is_straight(self):
    self.sort()
    if (set(A_straight) <= set([self[i].number for i in range(7)])):
        number[0] = 1
        return True 
    for i in range(10):
        normal_straight = [i, i+1, i+2, i+3, i+4]
        if (set(normal_straight) <= set([self[i].number for i in range(7)])):
            number[0] = 1 if i == 1 else i+4
            return True
    return False
Hand.is_straight = is_straight

#スリーカード
def is_three_of_a_kind(self):
    self.sort()
    num = collections.Counter([self[i].number for i in range(7)])
    value = num.most_common()
    if value[0][1] == 3:
        number[0] = value[0][0]
        return True
    else:
        return False
Hand.is_three_of_a_kind = is_three_of_a_kind

#ツーペア
def is_two_pair(self): # including four-of-a-kind 
    self.sort()
    if (self[0].number == self[1].number):
        for i in range(2,6):
            if(self[i].number == self[i+1].number):
                number[0] = max(self[0].number,self[i].number) 
                number[1] = min(self[0].number,self[i].number)
                if number[1] == 1:
                    number[1] = number[0]
                    number[0] = 1 
                return True
    elif(self[1].number == self[2].number):
        for i in range(3,6):
            if(self[i].number == self[i+1].number):
                number[0] = max(self[1].number,self[i].number) 
                number[1] = min(self[1].number,self[i].number)
                if number[1] == 1:
                    number[1] = number[0]
                    number[0] = 1                
                return True
    elif(self[2].number == self[3].number):
        for i in range(4,6):
            if(self[i].number == self[i+1].number):
                number[0] = max(self[2].number,self[i].number) 
                number[1] = min(self[2].number,self[i].number)
                if number[1] == 1:
                    number[1] = number[0]
                    number[0] = 1                
                return True
    elif(self[3].number == self[4].number):
        if(self[5].number == self[6].number):
            number[0] = max(self[3].number,self[5].number) 
            number[1] = min(self[3].number,self[5].number)
            if number[1] == 1:
                number[1] = number[0]
                number[0] = 1            
            return True        
    return False
Hand.is_two_pair = is_two_pair

#ワンペア
def is_one_pair(self):
    self.sort()
    for i in range(6):
        if self[i].number == self[i+1].number:
            number[0] = self[i].number
            return True
    return False
Hand.is_one_pair = is_one_pair

#ハイカード(役無し)
def is_high_card(self):
    self.sort()
    if self[0].number == 1:
        return self[0].number
    else:
        return self[6].number
Hand.is_high_card = is_high_card

"""役の決定 return は役の名前と、その役を構成している数字"""
def poker_hand_deter(self):
    poker_hand_list = [" ","high card","one pair","two pair","three of a kind",
                        "straight","flush","full house","straight flush","four of a kind","royal straight flush"]

    if self.is_royal_straight_flush():
        return [poker_hand_list[10],number[0]]
    if self.is_four_of_a_kind():
        return [poker_hand_list[9],number[0]]
    elif self.is_flush() and self.is_straight():
        return [poker_hand_list[8],number[0]]
    elif self.is_full_house():
        return [poker_hand_list[7],number]
    elif self.is_flush():
        return [poker_hand_list[6],number[0]]
    elif self.is_straight():
        return [poker_hand_list[5],number[0]]
    elif self.is_three_of_a_kind():
        return [poker_hand_list[4],number[0]]
    elif self.is_two_pair():
        return [poker_hand_list[3],number]
    elif self.is_one_pair():
        return [poker_hand_list[2],number[0]]
    elif self.is_high_card():
        return [poker_hand_list[1], self.is_high_card()]
    else:
        return False
Hand.poker_hand_deter = poker_hand_deter   

'''
is_flush
is_straight
is_three_of_a_kind
is_two_pair
is_one_pair
'''

