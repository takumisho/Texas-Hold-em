#!/usr/bin/env python3
import unittest
import copy
from pcard import PlayingCard
from hand import Hand
import poker
from probability import *

"""実際にプログラム出来ているかのテスト"""
class TestPlayingCard(unittest.TestCase):

#   役の判定が正しく出来ているかのテスト
    def test_poker_hand(self):
        hand = Hand()
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 d5 h7")    # 12 high
        assert ['high card', 1] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 s7 h9")      # one pair
        assert ["one pair", 4] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 h7 d4")    # one pair
        assert ["one pair", 1] == hand.poker_hand_deter()        
        hand.set_up("♠9 ♢9 ♡1 ♡4 ♣8 s7 c9")      # three of a kind
        assert ["three of a kind", 9] == hand.poker_hand_deter()
        hand.set_up("♡12 ♠1 ♢12 ♠3 ♣12 h2 h8")   # three of a kind
        assert ["three of a kind", 12] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢1 ♡1 ♡9 ♣1 h6 d9")      # four of a kind
        assert ["four of a kind", 1] == hand.poker_hand_deter()
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣K dJ c9")      # four of a kind
        assert ["four of a kind", 9] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♡1 d10 c8")      # two pair
        assert ["two pair", [1,4]] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢1 c5 h3 ♡4 ♣4 ♡10")     # two pair
        assert ["two pair", [1,4]] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢2 ♡2 ♣4 ♡4 s9 dQ")      # two pair
        assert ["two pair", [4,2]] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢1 ♣10 ♡6 h8 d9 ♣9")    # two pair
        assert ["two pair", [1,9]] == hand.poker_hand_deter()
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣1 c7 h9")    # full house
        assert ["full house", [1,10]] == hand.poker_hand_deter()
        hand.set_up("♢3 ♣2 h7 s6 ♡3 ♠2 ♠3")      # full house
        assert ["full house", [3,2]] == hand.poker_hand_deter()
        hand.set_up("♢1 ♣7 h1 s7 ♡7 ♠1 ♠3")      # full house
        assert ["full house", [1,7]] == hand.poker_hand_deter()
        hand.set_up("♣2 ♢12 ♣6 ♣11 ♣13 h5 h3")   # 13 high not straight
        assert ['high card', 13] == hand.poker_hand_deter()
        hand.set_up("♠2 ♢3 ♡4 ♠1 h2 d10 ♠5")      # straight
        assert ["straight", 1] == hand.poker_hand_deter()
        hand.set_up("♠12 ♢9 ♣11 ♢8 ♡10 s3 h1")   # straight
        assert ["straight", 12] == hand.poker_hand_deter()
        hand.set_up("h10 h11 ♠10 ♢11 ♡12 ♠13 ♠1")  # straight
        assert ["straight", 1] == hand.poker_hand_deter()
        hand.set_up("h10 h5 ♠10 ♢4 ♡2 ♠3 ♠6")  # straight
        assert ["straight", 6] == hand.poker_hand_deter()
        hand.set_up("♠13 ♠2 ♠1 ♠8 ♠9 s7 h9")     # flush
        assert ["flush", 1] == hand.poker_hand_deter()
        hand.set_up("♠1 ♠11 ♠10 ♠13 ♠12 h12 d5")  # royal straight flush
        assert ["royal straight flush", 1] == hand.poker_hand_deter()
        hand.set_up("♢1 ♢5 ♢2 ♢4 ♢3 d9 h4")      # straight flush
        assert ["straight flush", 1] == hand.poker_hand_deter()

#   手札を引けていること＋役の判定＋勝率計算がちゃんと出来ているかのテスト
#   上のテストに全て print(Probability().hand_percent(hand)) をつけて確認済み
    def test_poker(self):
        hand = Hand()
        hand.set_up(hand)
        print("\n", hand)
        print(hand.poker_hand_deter())        
        print(Probability().hand_percent(hand))


#   自分が入力したものを判定したい場合
""" def test_input_poker(self):

        hand = Hand()
        hand.set_up()
        print(hand.poker_hand_deter())        
        print(Probability().hand_percent(hand))"""

if __name__ == "__main__":
    unittest.main()

