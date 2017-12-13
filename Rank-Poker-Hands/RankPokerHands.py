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

    Work out the Type of Hand; straight, flush, four of kind
    Score the type of hand

    If type of hand is the same
    Score the cards in the hand e.g. in Full House compare the 3 of kind cards
    then the 2 of kind cards, etc.

    If the hand type and hand cards are equal compare the kickers, highest to
    lowest. Kickers are cards NOT in the hand e.g. a hand of 3 of a kind the 
    other two cards are the kickers.
    """

    LOSS = "Loss"
    TIE = "Tie"
    WIN = "Win"
    card_values = { 
            '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,
            '8': 8,  '9': 9,  'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
            }

    STRAIGHT_FLUSH = 8
    FOUR_OF_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_KIND = 3
    TWO_PAIR = 2
    PAIR = 1

    #ace_high_map = dict(value_map).update({ 'A': 14})
    #ace_low_map = dict(value_map).update({ 'A': 1 })

    def __init__(self, hand):
        self.hand = hand.strip().split()
        self.values = sorted([self.card_values[card[0]] for card in self.hand])
        self.counts = {value: self.values.count(value) for value in self.values}
        self.hand_cards = []
        self.kickers=[]

    def pop_count(self, count):
        for key in self.counts.keys():
            if self.counts[key] == count:
                self.counts.pop(key)
                return key

    def is_flush(self):
        suit = [card[1] for card in self.hand]
        if (suit.count(suit[0]) == 5):
            self.hand_cards = sorted(self.counts.keys(), reverse=True)
            return True
        return False

    def is_straight(self):
        # If not all individual cards, can't be a straight.
        if self.counts.values().count(1) != 5:
            return False

        # Ace High Straight
        if (5 * (self.values[0] + self.values[0]+4)/2) == sum(self.values):
            self.hand_cards = self.values
            return True

        # Ace Low Straight
        ace_low_values = dict(self.card_values)
        ace_low_values['A'] = 1
        values = sorted([ace_low_values[card[0]] for card in self.hand])
        if (5 * (values[0] + values[0]+4)/2) == sum(values):
            self.hand_cards = values
            return True

        return False

    def is_four_of_kind(self):
        if (4 in self.counts.values()):
            self.hand_cards.append(self.pop_count(4))
            self.kickers.append(self.pop_count(1))
            return True
        return False

    def is_full_house(self):
        if (2 in self.counts.values() and 3 in self.counts.values()):
            self.hand_cards.append(self.pop_count(3))
            self.hand_cards.append(self.pop_count(2))
            return True
        return False

    def is_three_of_kind(self):
        if (3 in self.counts.values()):
            self.hand_cards.append(self.pop_count(3))
            self.kickers = self.counts.keys()
            return True
        return False

    def is_two_pair(self):
        if (list(self.counts.values()).count(2) == 2):
            self.hand_cards.append(self.pop_count(2))
            self.hand_cards.append(self.pop_count(2))
            self.kickers.append(self.pop_count(1))
            self.hand_cards = sorted(self.hand_cards, reverse=True)
            return True
        return False

    def is_pair(self):
        if (list(self.counts.values()).count(2) == 1):
            self.hand_cards.append(self.pop_count(2))
            self.kickers.append(self.counts.keys())
            return True
        return False

    def score_hand(self):
        if self.is_straight() and self.is_flush():
            return self.STRAIGHT_FLUSH
        elif self.is_four_of_kind():
            return self.FOUR_OF_KIND
        elif self.is_full_house():
            return self.FULL_HOUSE
        elif self.is_flush():
            return self.FLUSH
        elif self.is_straight(): 
            return self.STRAIGHT
        elif self.is_three_of_kind():
            return self.THREE_OF_KIND
        elif self.is_two_pair():
            return self.TWO_PAIR
        elif self.is_pair():
            return self.PAIR
        else:
            self.hand_cards = sorted(self.counts.keys(), reverse=True)
            return 0

    def compare_kickers(self, other):
        my_hand = sorted(self.kickers, reverse=True)
        their_hand = sorted(other.kickers, reverse=True)
        print "My Kickers: {}, Their Kickers: {}".format(my_hand, their_hand)
        for mine, theirs in zip(my_hand, their_hand):
            print "Mine: {}, Theirs: {}".format(mine, theirs)
            if mine > theirs:
                return self.WIN
            elif mine < theirs:
                return self.LOSS
        return self.TIE

    def compare_hands(self, other):
        my_hand = self.hand_cards
        their_hand = other.hand_cards
        print "My Hand: {}, Their Hand: {}".format(my_hand, their_hand)
        for mine, theirs in zip(my_hand, their_hand):
            print "Mine: {}, Theirs: {}".format(mine, theirs)
            if mine > theirs:
                return self.WIN
            elif mine < theirs:
                return self.LOSS
            #otherwise it's a tie, iterated for the next comparison
        return self.compare_kickers(other)

    def compare_with(self, other):
        my_hand = self.score_hand()
        their_hand = other.score_hand()
        print "My Hand: {}, Their Hand: {}".format(my_hand, their_hand)
        if my_hand > their_hand:
            return self.WIN
        elif my_hand < their_hand:
            return self.LOSS

        return self.compare_hands(other)

