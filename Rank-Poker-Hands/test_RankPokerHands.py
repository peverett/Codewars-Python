#!/usr/python
"""Test the PokerHand class for ranking poker hands."""

from RankPokerHands import PokerHand

class TestPokerHands(object):

    def runTest(self, expected, hand, other):
        player = PokerHand(hand) 
        opponent = PokerHand(other)
        assert player.compare_with(opponent) == expected

    def test_highest_flush(self):
        "Highest straight flush wins"
        self.runTest("Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
    
    def test_straight_flush(self):
        "Straight flush wins of 4 of a kind"
        self.runTest("Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")

    def test_highest_4_of_a_kind(self):
        "Highest 4 of a kind wins"
        self.runTest("Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")

    def test_4oak_over_fh(self):
        "4 Of a kind wins of full house"
        self.runTest("Loss", "2S AH 2H AS AC", "JS JD JC JH AD")

    def test_fh_over_flush(self):
        "Full house wins of flush"
        self.runTest("Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")

    def test_highest_flush(self):
        "Highest flush wins"
        self.runTest("Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")

    def test_flush_over_straight(self):    
        "Flush wins of straight"
        self.runTest("Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")

    def test_equal_straight(self):
        "Equal straight is tie"
        self.runTest("Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")

    def test_straight_over_3oak(self):
        "Straight wins of three of a kind"
        self.runTest("Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")

    def test_3oak_over_2pair(self):
        "3 Of a kind wins of two pair"
        self.runTest("Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")

    def test_2pair_over_pair(self):
        "2 Pair wins of pair"
        self.runTest("Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")

    def test_highest_pair(self):
        "Highest pair wins"
        self.runTest("Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")

    def test_pair_over_nothing(self):
        "Pair wins of nothing"
        self.runTest("Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")

    def test_highest_card_loses(self):
        "Highest card loses"
        self.runTest("Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")

    def test_highest_card_wins(self):
        "Highest card wins"
        self.runTest("Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")

    def test_qual_cards_tie(self):
        "Equal cards is tie"
        self.runTest("Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")

    def test_3oak_highest_wins(self):
        "3 of Kind highest Win wins"
        # Even though the 'other' hand has a higher 3 of a kind
        # It loses when just comparing the card score, which is wrong
        self.runTest("Loss", "2S 2H 2D AC KC", "3S 3S 3C 2S 4S")

