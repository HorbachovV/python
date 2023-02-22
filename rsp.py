import random
from secrets import choice

def get_choices():
    player_choice = input('Enter a choice: rock, paper, scissors: ')
    options = ['rock', 'paper', 'scissors'] #list
    computer_choice = random.choice(options)
    choice = {'player': player_choice, 'computer': computer_choice} #dictionar
    return choice

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    # print('You chose ' + player + ", computer chose " + computer)
    if player == computer:
        return 'It is a tie'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win'
        else: 
            return 'Paper covers rock! You lose'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win'
        else: 
            return 'Scissors cut paper! You lose'
    elif player == 'scisors':
        if computer == 'paper':
            return 'Scissors cut paper! You win'
        else: 
            return 'Rock smashes scisors! You lose'
        
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)


