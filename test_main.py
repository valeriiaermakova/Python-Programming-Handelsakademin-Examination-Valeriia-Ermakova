from Classes_and_functions import choose_winner, Human, Dealer


# checking who is defned as winner since it is core bussiness logic and affects potential profit/losses
def test_should_define_dealer_as_winner():
    user = Human()
    dealer = Dealer()
    user_score = 12
    dealer_score = 18
    result = choose_winner(user_score, dealer_score, user, dealer)
    assert result == "\nDu förlorade. Dealern är vinnare!"


def test_should_define_player_as_winner():
    user = Human()
    dealer = Dealer()
    user_score = 20
    dealer_score = 19
    result = choose_winner(user_score, dealer_score, user, dealer)
    assert result == "\nDu är vinnare!"


def test_should_check_tie_condition():
    user = Human()
    dealer = Dealer()
    user_score = 18
    dealer_score = 18
    result = choose_winner(user_score, dealer_score, user, dealer)
    assert result == "\nDet är oavgjort."


# checking that computer does not stop rolling before reasching treshhold value since it is important bussiness logic and affects potential profit/losses
def test_should_check_that_computer_not_rolling_less_than_treshhold():
    dealer = Dealer()
    dealer.roll(17)
    assert dealer.score >= 17


# checking that corresponding function catches immediate loss when player/dealer reaches 21 since it is core rule of the game
def test_should_check_immediate_lost_boolean_for_human():
    user = Human()
    user.score = 21
    result = user.is_met_epic_loss_condition()
    assert result == True


def test_should_check_immediate_lost_boolean_for_dealer():
    user = Dealer()
    user.score = 22
    result = user.is_met_epic_loss_condition()
    assert result == True
