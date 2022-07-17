#!/usr/bin/env python3
import unittest
import copy
from pcard import PlayingCard
from hand import Hand
import poker
from probability import *

"""実際にプログラム出来ているかのテスト"""
class TestPlayingCard(unittest.TestCase):
    """test PlayingCard class"""

    """def test_is_four_of_a_kind(self):
        hand = Hand()
        # False
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 ♣5 ♣8")
        self.assertFalse(hand.is_four_of_a_kind())
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣1 ♣5 ♡7")    # full house
        self.assertFalse(hand.is_four_of_a_kind())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣8 s2 s6")      # three of a kind
        self.assertFalse(hand.is_four_of_a_kind())
        # True
        hand.set_up("♠1 ♢1 h1 h9 c1 h7 h8")
        self.assertTrue(hand.is_four_of_a_kind())
        hand.set_up("♠9 ♢9 h1 h9 c9 d3 s6")
        self.assertTrue(hand.is_four_of_a_kind())

    def test_is_full_house(self):
        hand = Hand()
        # False
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 s7 d8")
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 c9 d12")
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣8 h6 d3")      # three of a kind
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠1 ♢1 ♡1 ♡9 ♣1 h7 s4")
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣9 h6 d8")
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣9 h2 d7")      # four of a kind
        self.assertFalse(hand.is_full_house())
        hand.set_up("♠1 ♢1 ♡1 ♡9 ♣1 h2 d7")      # four of a kind
        self.assertFalse(hand.is_full_house())
        # True
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣1 s10 d7")    # full house
        self.assertTrue(hand.is_full_house())
        hand.set_up("♢3 ♣2 ♡3 ♠2 ♠3 s6 h8")      # full house
        self.assertTrue(hand.is_full_house())

    def test_is_three_of_a_kind(self):
        hand = Hand()
        # False
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 s8 d9")      # one pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 h11 h5")    # one pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♡1 d9 d12")      # two pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠1 ♢1 ♡4 ♣4 ♡10 h12 s6")     # two pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠1 ♢2 ♡2 ♣4 ♡4 s6 s10")      # two pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣9 c5 s5")    # two pair
        self.assertFalse(hand.is_three_of_a_kind())
        hand.set_up("♠2 ♢3 ♡4 ♠1 ♠5 s8 d6")      # straight
        self.assertFalse(hand.is_three_of_a_kind())
        # True
        hand.set_up("♡12 ♠1 ♢12 ♠3 ♣12 s8 h9")   # three of a kind
        self.assertTrue(hand.is_three_of_a_kind())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣8 h4 s12")      # three of a kind
        self.assertTrue(hand.is_three_of_a_kind())

    def test_is_flush(self):
        hand = Hand()
        # False
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 ♡4 ♠5")    # 12 high
        self.assertFalse(hand.is_flush())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 ♣9 ♣8")      # one pair
        self.assertFalse(hand.is_flush())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣8 d4 s7")      # three of a kind
        self.assertFalse(hand.is_flush())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♡1 s6 h9")      # two pair
        self.assertFalse(hand.is_flush())
        hand.set_up("♣2 ♢12 ♣1 ♣11 ♣13 h3 d7")   # 13 high not straight
        self.assertFalse(hand.is_flush())
        # True
        hand.set_up("♠13 ♠2 ♠4 ♠8 ♠9 h4 d6")     # flush
        self.assertTrue(hand.is_flush())

    def test_is_straight(self):
        hand = Hand()
        # False
        hand.set_up("♣2 ♢12 ♣1 ♣11 ♣13 ♢5 ♢8")   # 13 high not straight
        self.assertFalse(hand.is_straight())
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 d6 h7")
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 hJ hK")
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 h6 d4")    # one pair
        self.assertFalse(hand.is_straight())
        hand.set_up("♠9 ♢9 ♡1 ♡9 ♣8 s4 c5")      # three of a kind
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢1 ♡1 ♡9 ♣1 c6 hQ")      # four of a kind
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♡1 d6 h9")      # two pair
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢2 ♡2 ♣4 ♡4 h10 c7")      # two pair
        self.assertFalse(hand.is_straight())
        hand.set_up("♠1 ♢1 ♣10 ♡10 ♣1 c8 c9")    # full house
        self.assertFalse(hand.is_straight())
        hand.set_up("♢3 ♣2 ♡3 ♠2 ♠3 d8 d6")      # full house
        self.assertFalse(hand.is_straight())
        # True
        hand.set_up("♠12 ♢9 ♣11 ♢8 ♡10 c3 c5")   # straight
        self.assertTrue(hand.is_straight())
        hand.set_up("♠2 ♢3 ♡4 ♠1 ♠5 h3 d2")      # straight
        self.assertTrue(hand.is_straight())
        hand.set_up("♠10 ♢11 ♡12 ♠13 ♠1 ♢12 ♢7")  # straight
        self.assertTrue(hand.is_straight())
        hand.set_up("♠10 ♢11 ♡12 ♠13 ♠9 ♢12 ♢7")  # straight
        self.assertTrue(hand.is_straight())

    def test_is_straight_flush(self):
        hand = Hand()
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 s6 h4")    # 12 high
        self.assertFalse(hand.is_straight_flush())
        hand.set_up("♠13 ♠2 ♠4 ♠8 ♠9 d6 c12")     # flush
        self.assertFalse(hand.is_straight_flush())
        hand.set_up("♠2 ♢3 ♡4 ♠1 ♠5 c9 h10")      # straight
        self.assertFalse(hand.is_straight_flush())
        # True
        hand.set_up("♢1 ♢5 ♢2 ♢4 ♢3 h4 c2")      # straight flush
        self.assertTrue(hand.is_straight_flush())
        hand.set_up("♠1 ♠11 ♠10 ♠13 ♠12 s4 h12")  # royal straight flush
        self.assertTrue(hand.is_straight_flush())

    def test_is_two_pair(self):
        hand = Hand()
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 h6 d3")    # 12 high
        self.assertFalse(hand.is_two_pair())
        hand.set_up("♠2 ♢3 ♡4 ♠1 ♠5 d6 s8")
        self.assertFalse(hand.is_two_pair())
        hand.set_up("♠1 ♢2 ♡4 ♣4 ♠5 s6 c7")
        self.assertFalse(hand.is_two_pair())
        # True
        hand.set_up("♠A ♢2 ♡4 ♣12 ♡12 ♣7 ♣4")
        self.assertTrue(hand.is_two_pair())
        hand.set_up("♠1 ♢1 ♡4 ♣7 ♡10 d10 h5")
        self.assertTrue(hand.is_two_pair())
        hand.set_up("♠1 ♢2 ♡2 ♣4 ♡4 s7 c9")
        self.assertTrue(hand.is_two_pair())

    def test_is_one_pair(self):
        hand = Hand()
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 d5 h7")    # 12 high
        self.assertFalse(hand.is_one_pair())
        hand.set_up("♠2 ♢3 ♡4 ♠1 ♠5 h6 d9")      # straight
        self.assertFalse(hand.is_one_pair())
        hand.set_up("♠13 ♠2 ♠4 ♠8 ♠9 d7 h5")     # flush
        self.assertFalse(hand.is_one_pair())
        # True
        hand.set_up("♠1 ♢2 ♡4 ♣12 ♠5 d8 s12")      # one pair
        self.assertTrue(hand.is_one_pair())
        hand.set_up("♠1 ♢12 ♣10 ♡9 ♣1 s6 s8")    # one pair
        self.assertTrue(hand.is_one_pair())
    
    def test_is_high_card(self):
        hand = Hand()
        hand.set_up("♣2 ♢12 ♣1 ♣10 ♣9 d5 h7")    # 12 high
        assert 12 == hand.is_high_card()"""


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

