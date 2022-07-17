#!/usr/bin/env python3
import unittest
import copy
from pcard import *
from hand import Hand
import poker
#please give me naitei
"""勝率計算のクラス"""
class Probability(list):

    def hand_percent(self,hand):
        value = [0,8.7,39.32,72.48,87.13,91.86,95.78,99.23,99.98,99.99,99.99]
        poker_hand_list = [" ","high card","one pair","two pair","three of a kind",
                        "straight","flush","full house","straight flush","four of a kind","royal straight flush"] 
        
#       役の名前 
        poker_hand_number = (poker_hand_list.index(hand.poker_hand_deter()[0]) - 1)

#       数字により、同じ役でも勝率が変わるため、その計算のための値
        number_percent = (value[poker_hand_number + 1 ] - value[poker_hand_number]) / 13

#       ツーペア、フルハウス等の2種類数字がある場合に使う        
        number_number_percent = (value[poker_hand_number + 1 ] - value[poker_hand_number]) / 169

#       ツーペア、フルハウス以外
        if type(hand.poker_hand_deter()[1]) == int:

            hand_number = hand.poker_hand_deter()[1]
            if hand_number == 1:
                hand_number = 14

            percent = (value[poker_hand_number] + number_percent * (hand_number - 2))

#       ツーペア、フルハウスの場合        
        if type(hand.poker_hand_deter()[1]) == list:

            hand_number = [hand.poker_hand_deter()[1][0],hand.poker_hand_deter()[1][1]]
            if hand_number[0] == 1:
                hand_number[0] = 14
                
            percent = (value[poker_hand_number] + (number_percent * (hand_number[0] - 2)) 
            + (number_number_percent * (hand_number[1] - 2)))

#       return        
        word = "勝率 " + str(percent) + "%"
        return  word
    


  