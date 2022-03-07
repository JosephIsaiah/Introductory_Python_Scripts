# Name: Bob's Tavern Trivia Game
# Date: May 11, 2021
# Purpose: This 'trivia game' uses a dictionary of trivia questions in key / value format. 
# It converts the keys to a list, allows the user to determine how many questions they want to challenge, 
# randomly selects the question from the list, asks for an answer, evaluates the user answer to the 
# dictionary value, and provides feedback for right / wrong, and total score.

import random

# created a dictionary with questions as keys and answers as values.
questions = {
'''How many computer-generated effects were used in the movie
Lord of the Rings -Return of the King?
1. 540
2. 799
3. 1205
4. 1488
'''
:'4',
'''In the movie "The Blues Brothers", what does Jake order at the diner?
1. A medium pizza with pineapple and ham
2. Three cheeseburgers with the works and a tall glass of milk
3. Four fried chickens and a Coke
4. A small Greek salad with extra feta, a steak (well done), 2 baked potatoes, and a coffee
'''
:'3',
'''In The Simpsons, what football team has Homer always wanted to own?
1. Washington Redskins
2. Dallas Cowboys
3. Denver Broncos
4. Cleveland Browns
'''
:'2',
'''In the TV show Seinfeld, what did Elaine decide was 'her song'?
1. I am Woman
2. Desperado
3. Yesterday
4. Witchy Woman
'''
:'4',
'''Babe Ruth debuted in professional baseball at the age of 19 years old with which team?
1. Boston Red Sox
2. New York Yankees
3. St Louis Browns
4. Cincinnati Reds
'''
:'1',
'''What nut is used to make marzipan?
1. Almonds
2. Peanuts
3. Cashews
4. Franklins
'''
:'1',
'''What is the most frequently sold item at Walmart?
1.  Beer
2.  Socks
3.  Banana
4.  Diapers
'''
:'3',
'''What is the most common color of toilet paper in France?
1.  White
2.  Cream
3.  Brown
4.  Pink
'''
:'4',
'''What is the total number of dots on a pair of dice?
1. 42
2. 36
3. 54
4. 24
'''
:'1',
'''What color are aircraft Black Boxes?
1. Red
2. Orange
3. Black
4. White
'''
:'2',
'''How many miles is New Zealand's Ninety Mile Beach?
1. 99
2. 90
3. 55
4. 139
'''
:'3'
}

# made a list of fun comments for correct answers
sarcastic = ['You go smarty pants!', 'Did you google that?', 'Wow, you are smarter than you look!', 
'Did you phone a Facebook friend?', 'You might be smarter than my five-year old. But probably not.',
'Have you seen these questions before?', 'Aren\'t you supposed to be working right now?',
'Bet it feels good to be right for once!', 'You\'re kinda like a genius! Kinda, but not really.', 
'Don\'t make it look too easy. You\'ll embarass the other players.', 'Really, you knew that?']

# provides the logic of the program
def logic():
    try:
        global right
        global wrong
        right = 0
        wrong = 0
        line  = '-' * 48
        value_list   = list(questions.keys())  # create a list of the dictionary keys
        sarcasm      = list(sarcastic)
        rounds       = int(input(f'\nHow many questions would you like ({len(value_list)} max): ')) # user determines number of questions from value provided
        while rounds == 0 or rounds > len(value_list): # prevent the program from running with zero or too may questions selected
            rounds   = int(input(f'Psst ... pick a number between 1 and {len(value_list)}: '))
        else: 
            for x in range(rounds): # loop will continue for the # of questions the user selected
                joke     = random.choice(sarcasm) # select random comment from list for use in the correct answer feedback
                question = random.choice(value_list) # once in a list, we can use random to select a 'key' to show as a user question
                for trivia, answer in questions.items(): # iterate over the dictionary get the correct value for the randomly selected key
                    if question == trivia:
                        correct_answer = answer

                print(line)      
                print(question)
                guess = input('Enter the correct number: ')
                print(line)
                if guess == correct_answer: # compare user input to the correct value determined above
                    right += 1
                    print(f'\nYou are right! That is {right} correct answers.\n{joke}\n') # randomly select from the sarcastic list
                    value_list.remove(question) # remove the question so that it is only asked once each round
                    sarcasm.remove(joke) # remove the comment from this round's list
                else:
                    wrong += 1
                    print(f'\nToo bad! The correct answer is {questions[question]}.\n') # if user is incorrect, show them the correct answer
                    # if we were using this for studying, we may want to remove the next line so that wrong answers are asked until correct
                    value_list.remove(question)
        play_again()
    except:
        print(f'Please pick a number between 1 and {len(value_list)}.')
        logic()

def play_again(): # function to allow the user to continue with a new round
    print(f'\nGood job smarty pants! You got {right} right and {wrong} wrong.')
    play = input('\nWanna try another round? (Y/N): ').lower()
    logic() if play == 'y' else end()

def end():
    input(f'\nThank you for playing.')

def main():
    print('Welcome to Bob\'s Tavern Trivia!')
    logic()

if __name__ == '__main__':
    main()

