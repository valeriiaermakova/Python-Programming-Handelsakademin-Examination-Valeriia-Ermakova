import random


class Player:
    def __init__(self):
        self.score = 0


class Human(Player):

    def roll(self):
        self.dice = random.randint(1, 6)
        self.score += self.dice
        print(f"Du rullade {self.dice}. Din score: {self.score}")
        return self.score


class Dealer(Player):

    def roll(self, max_treshhold):
        while self.score <= max_treshhold:
            self.dice = random.randint(1, 6)
            self.score += self.dice
            print(f"Dealern rullade {self.dice}. Dealers  score: {self.score}")
        return self.score


def choose_winner(user_score, dealer_score):
    if user_score > dealer_score:
        print("Du är vinnare!")
    elif user_score < dealer_score:
        print("Du förlorade. Dealern är vinnare!")
