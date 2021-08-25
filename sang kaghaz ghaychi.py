print("")
print("Let's play a Rock-Paper-Scissors Game...")
print("To left the game, just send exit or e")
print("")

while True: 
    player = input('Rock Paper Scissors? ') 
    player = optimizeChoice(player) 

    
    if player == 'exit':
        break
    
    
    if not validateInput(player):
        print('Your choice is not valid!!!!!')
        continue

    
    computer = generateComputerChoince()
    print(f"I choiced {computer}")

    
    winner = getWinner(player, computer);
    
    
    if winner == WINNER_PLAYER:
        print("Congratulation... You Win!!!!!")
    elif winner == WINNER_COMPUTER:
        print("Sorry... You lost!!!!!")
    elif winner == WINNER_TIE:
        print("Ops... That's a Tie!!!!!")
    else:
        print("Erro 404 Winner NOT Found!!!!")

    
    print("")
    print("Let's play again...")
    print("")


print('Bye... See ya later!!!!!')