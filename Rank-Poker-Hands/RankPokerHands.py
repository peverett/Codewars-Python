#!/usr/python
"""
A famous casino is suddenly faced with a sharp decline of their revenues. They
decide to offer Texas hold'em also online. Can you help them by writing an
algorithm that can rank poker hands?

Task:

Create a poker hand that has a method to compare itself to another poker hand:
    compare_with(self, other_hand)

A poker hand has a constructor that accepts a string containing 5 cards:
    PokerHand(hand)

The characteristics of the string of cards are:
* A space is used as card seperator
* Each card consists of two characters
* The first character is the value of the card, valid characters are: 
  2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
* The second character represents the suit, valid characters are: 
* S(pades), H(earts), D(iamonds), C(lubs)

The result of your poker hand compare can be one of these 3 options:
    RESULT = ["Loss", "Tie", "Win"]

Apply the Texas Hold'em rules for ranking the cards.
There is no ranking for the suits.

https://www.briggsoft.com/docs/pmavens/PMHoldem.htm
"""

class PokerHand(object):
    """Design

    The type of hand is given a score, according to what hand beats what.
    The score of the cards IN that hand is calculated, so that hands of the
    same time can be compared.
    Whatever cards are left are also scored in the case of everything being
    equal e.g. two hands with a pair being the same pair - who wins!
    """

    LOSS = "Loss"
    TIE = "Tie"
    WIN = "Win"
    value_map = { 
            '1': 1,  '2': 2,  '3': 3,  '4': 4,
            '5': 5,  '6': 6,  '7': 7,  '8': 8,
            '9': 9,  'T': 10, 'J': 11, 'Q': 12, 
            'K': 13, 'A': 14 
            }

    def __init__(self, hand):
        self.hand = hand.strip().split()
        self.values = [PokerHand.value_map[card[0]] for card in self.hand]
        self.values.sort()
        self.counts = {value: self.values.count(value) for value in self.values}
        self.card_score = sum(self.values)
        self.hand_score = self.score_hand()

    def is_flush(self):
        suit = [card[1] for card in self.hand]
        return (suit.count(suit[0]) == 5)

    def is_straight(self):
        for index in range(1,5):
            if self.values[index-1] + 1 != self.values[index]:
                return False
        return True

    def is_four_of_kind(self):
        return (4 in self.counts.values())

    def is_full_house(self):
        return (2 in self.counts.values() and 3 in self.counts.values())

    def is_three_of_kind(self):
        return (3 in self.counts.values())

    def is_two_pair(self):
        return (list(self.counts.values()).count(2) == 2)

    def is_pair(self):
        return (list(self.counts.values()).count(2) == 1)

    def score_hand(self):
        if self.is_straight() and self.is_flush():
            return 8
        elif self.is_four_of_kind():
            return 7
        elif self.is_full_house():
            return 6
        elif self.is_flush():
            return 5
        elif self.is_straight(): 
            return 4
        elif self.is_three_of_kind():
            return 3
        elif self.is_two_pair():
            return 2
        elif self.is_pair():
            return 1
        else:
            return 0

    def compare_with(self, other):
        if self.hand_score > other.hand_score:
            return self.WIN
        elif self.hand_score < other.hand_score:
            return self.LOSS
        else:
            if self.card_score > other.card_score:
                return self.WIN
            elif self.card_score < other.card_score:
                return self.LOSS
       
        return self.TIE

