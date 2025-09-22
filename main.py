import Classes_and_functions

print(
    """Välkommen till Tärningsspelet 21!\n
    Du behöver slå tärningarna tills du är så nära till 21 poäng som möjligt utan att gå över.  Efter det vår Dealer rullar.
    Man förlorar så snart som man når 21 poäng och annars vinner den som är närmast 21. 
    Du kan skriva 'rulla' för att rulla tärningen (värde 1-6) eller 'stanna' för att skicka turen till dealern eller 'avsluta' om du vill inte spella längre. Inga citattecken behövs.
    Lycka till!\n"""
)

user_choice = 0
player1 = Classes_and_functions.Human()
player2 = Classes_and_functions.Dealer()

while user_choice != "avsluta":
    user_choice = input("Skriva om du vill rulla, stanna eller avsluta:")
    if user_choice == "rulla":
        final_user_score = player1.roll()

        if final_user_score >= 21:
            print(
                f"Tyvärr, förlorade du det här spelet!\nDin score är {player1.score} som är mer eller lika 21.\nVi börjar over!"
            )
            player1.score = 0
            player2.score = 0
            continue

    if user_choice == "stanna":

        final_dealer_score = player2.roll(17)

        if final_dealer_score >= 21:
            print(f"Du är vinnare!\n Dealern fick 21 eller mer! Vi börjar over!")
            player1.score = 0
            player2.score = 0
            continue
        else:
            Classes_and_functions.choose_winner(final_user_score, final_dealer_score)
