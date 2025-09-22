import Classes_and_functions
from Classes_and_functions import print_win_count

print(
    """Välkommen till Tärningsspelet 21!\n
    Du behöver slå tärningarna tills du är så nära till 21 poäng som möjligt utan att gå över. Efter det vår Dealer rullar.
    Man förlorar så snart som man når 21 poäng och annars vinner den som är närmast 21. 
    Du kan skriva 'rulla' för att rulla tärningen (värde 1-6) eller 'stanna' för att skicka turen till dealern eller 'avsluta' om du vill inte spella längre. Inga citattecken behövs.
    Lycka till!\n"""
)

user_choice = 0
game_options = ["rulla", "stanna", "avsluta"]
player1 = Classes_and_functions.Human()
player2 = Classes_and_functions.Dealer()

while user_choice != "avsluta":
    user_choice = input("Skriva om du vill rulla, stanna eller avsluta:").lower()
    if user_choice not in game_options:
        print(
            "Error: Du skrev alternativ som inte stöds.\nFörsök igen och se till att du skriver något av följande untan citattecken eller andra symboler:\nrulla, stanna, avsluta.\nOroa dig inte, din progress är sparad."
        )

    if user_choice == "rulla":
        final_user_score = player1.roll()
        if player1.is_met_epic_loss_condition():
            print("Du har nått 21 poäng och förlorade. Dealern är vinnare!")
            player2.win_count += 1
            player1.score = 0
            player2.score = 0
            print_win_count(player1, player2)
            continue

    if user_choice == "stanna":

        final_dealer_score = player2.roll(17)

        if player2.is_met_epic_loss_condition():
            print(f"Du är vinnare! Dealern fick 21 eller mer poäng!")
            player1.win_count += 1
            player1.score = 0
            player2.score = 0
            print_win_count(player1, player2)
            continue
        else:
            Classes_and_functions.choose_winner(
                final_user_score, final_dealer_score, player1, player2
            )
            print_win_count(player1, player2)
