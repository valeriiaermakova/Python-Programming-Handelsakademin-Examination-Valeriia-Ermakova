import random


class Player:
    def __init__(self):
        self.score = 0
        self.win_count = 0

    def roll(self):
        pass

    def is_met_epic_loss_condition(self):
        return self.score >= 21


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


def choose_winner(user_score, dealer_score, user, dealer):
    if user_score > dealer_score:
        print("Du är vinnare!")
        user.win_count += 1
    elif user_score < dealer_score:
        print("Du förlorade. Dealern är vinnare! ")
        dealer.win_count += 1
    else:
        print("Det är oavgjort.")


def print_win_count(user, dealer):
    print(f"Du vann {user.win_count} spel och dealern vann {dealer.win_count} spel.")
    if user.win_count > dealer.win_count:
        print("Du leder! Bra jobbat! Låt oss fortsätta i nästa omgång!")
    elif dealer.win_count > user.win_count:
        print("Du kommer efter. Ge inte upp! Försök igen!")
    else:
        print("Det är oavgjort. Vem ska vinna nästa gång?")
