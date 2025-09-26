import random


class Player:
    def __init__(self):
        self.score = 0
        self.win_count = 0

    def roll(self):  # defined in subclasses
        pass

    # defines immidiate loss when we do not need to proceed with results comparison
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
        # function takes as a parameter a number at reaching which computer/dealer should stop rolling
        while self.score <= max_treshhold:
            self.dice = random.randint(1, 6)
            self.score += self.dice
            print(f"Dealern rullade {self.dice}. Dealers  score: {self.score}")
        return self.score


# this function is not part of class since win condition is separate entity from Player instances
def choose_winner(user_score, dealer_score, user, dealer):
    if user_score > dealer_score:
        result = "\nDu är vinnare!"
        user.win_count += 1
    elif user_score < dealer_score:
        result = "\nDu förlorade. Dealern är vinnare!"
        dealer.win_count += 1
    else:
        result = "\nDet är oavgjort."
    # print(result)
    return result


# this function is not part of class since print win count is separate entity from Player instances
def give_win_count(user, dealer, file):
    win_count_output = (
        f"\nDu vann {user.win_count} spel och dealern vann {dealer.win_count} spel.\n"
    )
    print(win_count_output)
    file.write(win_count_output)
    if user.win_count > dealer.win_count:
        result = "Du leder! Bra jobbat! Låt oss fortsätta i nästa omgång!\n"
    elif dealer.win_count > user.win_count:
        result = "Du kommer efter. Ge inte upp! Försök igen!\n"
    else:
        result = "Det är oavgjort. Vem ska vinna nästa gång?\n"
    # print(result)
    return result
