# File: 2252_McnamaraJ_Lesson4#_InLab.py
# Name: Rock Paper Scissor
# Author: Joseph McNamara
# Date: April 18, 2021
# Purpose: This program replicates the game Rock,
# Paper, Scissor, with a focus on building with functions.

import random
#set global variables
player_name = str
player_choice = str
player_score = 0
computer_choice = 0
computer_score = 0
tie_score = 0
round = 0

#function to randomly pick the computers choice of rock, paper, scissor
def computer_pick():
    global computer_choice
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = 'rock'
    elif computer_choice == 2:
        computer_choice = 'paper'
    elif computer_choice == 3:
        computer_choice = 'scissor'
    return computer_choice

#players name
def players_name():
    global player_name
    player_name = input('Enter player\'s name: ')
    return player_name
   
#show computers choice
def show_computer():
    print('-' * 48)
    print(f'The computer picked {computer_choice}.')
    print('-' * 48)
   
#Ask player for choice and save to global variable
def player_pick(player_name):
    global player_choice
    player_choice = input(f'Ok {player_name}, choose rock, paper, or scissor: ').lower()
    return player_choice
   
#compare player and computer choice, determine winner, add round to count
def determine_winner(player, computer, name):
    global player_score
    global computer_score
    global tie_score
    global round
    if (player == 'rock' and computer == 'scissor') or (player == 'scissor' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        print(f'{name}, you win!\n')
        player_score += 1
        round += 1
    elif (computer == 'rock' and player == 'scissor') or (computer == 'scissor' and player == 'paper') or (computer == 'paper' and player == 'rock'):
        print(f'{name}, you lose!\n')
        computer_score += 1
        round += 1
    elif computer == player:
        print('It is a draw! Play again.\n')
        tie_score += 1
        round += 1

#show score
def score():
    print(f'\n*** {player_name} {player_score} vs. Computer {computer_score}. Ties: {tie_score} ***')

#option for player to continue playing
def play_again():
    play = input('Would you like to play again (Y/N):').lower()
    if play == 'y':
        game()
    else:
        final()
       
#show number of rounds and final score
def final():
    print('-' * 48)
    print(f'You played {round} rounds.\nFinal Score: {player_name} {player_score} vs. Computer {computer_score}')
    print('Thank you for playing!')
    print('-' * 48)
   
#define main function calling on above functions
def game():
    computer_pick()
    player_pick(player_name)
    show_computer()
    determine_winner(player_choice, computer_choice, player_name)
    score()
    play_again()

#verify code is in main memmory and call game functions
if __name__ == '__main__':
    players_name()
    game()

'''Note: My first draft of this code was written without functions. This version is
perhaps over functioned and is actually 20 lines longer than the non-function version. 
However, if we were making a series of games most of these functions could be reused 
in other applications. One problem I was not able to resolve was making the game autoplay 
after a tie. Any advice or guidance on that topic is much appreciated.
'''