# Name: State Abbreviation Quiz
# Date: April 30, 2021
# Purpose: This program shows the user a random state name abbreviation and asks 
# the user to spell the full state name. The program then provides a score of right 
# and wrong, plus a list of missed states.

import random

# ceate a dictionary of states and state name abbreviations 
states = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME',
    'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH','New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
    'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }

# set global variables
value_list = list(states.values())
right  = 0 
missed = []

# function that chooses our random value (state abreviation)
def random_state():
    global state_abrev # not exactly clear why I can create this variable within this function, but could not do the same thing with "right" in the quiz function.
    state_abrev = random.choice(value_list)
    return state_abrev

# ask user to spell the state, state if correct, keep score, and make list of missed states
def quiz():
    global right
    global missed
    guess = input(f'Type the state abbreviated as: {state_abrev}   ')
    if guess == state_name:
        print(f'Great Job. {state_abrev} is short for {state_name}.\n')
        right += 1
    else:
        print(f'Too bad! The state abbreviated as {state_abrev} is {state_name}.\n')
        missed.append(state_name)
    play_again()

# use the value (state abbreviation) to determine the key (full state name) from our dictionary    
def get_key(val):
    global state_name
    for name, abreviation in states.items():
        if val == abreviation:
            state_name = name
            return state_name

# offer the user the option to play again
def play_again():
    play = input('Let\'s try another state! (Y/N): ').lower()
    main() if play == 'y' else end() # used ternary operator to streamline the code

# provide closing for the program and show the user their score and the states they missed
def end():
    print(f'\nGood job practicing! You knew {right} states names. You missed {len(missed)} states. ')
    input(f'Keep working on the following: {", ".join(missed)}\n')
   
def main():
    random_state()
    get_key(state_abrev)
    quiz()
   

if __name__ == "__main__":
    main()
