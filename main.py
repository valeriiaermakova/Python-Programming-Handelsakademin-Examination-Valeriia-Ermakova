from Classes_and_functions import Human, Dealer, choose_winner, give_win_count

# welcoming and introduction message, prints once at the beginning of the game
print(
    """Välkommen till Tärningsspelet 21!\n
    Du behöver slå tärningarna tills du är så nära till 21 poäng som möjligt utan att gå över. Efter det vår Dealer rullar.
    Man förlorar så snart som man når 21 poäng och annars vinner den som är närmast 21. 
    Du kan skriva 'rulla' för att rulla tärningen (värde 1-6) eller 'stanna' för att skicka turen till dealern eller 'avsluta' om du vill inte spella längre. Inga citattecken behövs.
    Lycka till!\n"""
)

user_choice = 0  # initialize user input to be able to use it straight away in "while" cycle condition
game_options = [
    "rulla",
    "stanna",
    "avsluta",
]  # listing valid game options to be able to print error message if user enters something else
player1 = Human()
player2 = Dealer()
file = open("results_of_last_game.txt", "w")

while user_choice != "avsluta":
    user_choice = input(
        "Skriva om du vill rulla, stanna eller avsluta: "
    ).lower()  # case insensitive user input
    if user_choice not in game_options:  # checking that user input is valid
        print(
            "Error: Du skrev alternativ som inte stöds.\nFörsök igen och se till att du skriver något av följande untan citattecken eller andra symboler:\nrulla, stanna, avsluta.\nOroa dig inte, din progress är sparad."
        )

    if user_choice == "rulla":
        # saving final user roll below to chose winner later
        final_user_score = player1.roll()
        if player1.is_met_epic_loss_condition():
            print("\nDu har nått 21 poäng och förlorade. Dealern är vinnare!")
            player2.win_count += 1
            player1.score = 0  # need to nullify roll count since new round of the game starts after this condition
            print(give_win_count(player1, player2, file))
            continue  # need to skip steps below and start a new cycle iteration since new round in game starts here

    if user_choice == "stanna":
        # check that player rolled first to be sure we have user result against which we compare winners
        if player1.score == 0:
            print("Du måste rulla själv innan dealern rullar!")
        else:
            # saving final dealer roll below to chose winner later
            final_dealer_score = player2.roll(17)

            if player2.is_met_epic_loss_condition():
                print(f"\nDu är vinnare! Dealern fick 21 eller mer poäng!")
                player1.win_count += 1
                player1.score = 0  # need to nullify roll count for both players since new round of the game starts after this condition
                player2.score = 0
                print(give_win_count(player1, player2, file))
                continue  # need to skip steps below and start a new cycle iteration since new round in game starts here
            else:
                print(
                    choose_winner(
                        final_user_score, final_dealer_score, player1, player2
                    )
                )
                print(give_win_count(player1, player2, file))
                final_user_score = 0
                player1.score = 0  # need to nullify roll count for both players since new round of the game starts after this condition
                player2.score = 0
file.close()
