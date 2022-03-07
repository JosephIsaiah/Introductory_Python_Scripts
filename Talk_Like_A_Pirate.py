# Name: Talk like a pirate
# Date: April 24, 2021
# Purpose: This program takes user inputed words 
# and converts them to a fictionalized pirate dialect.

import random

# created a dictionary for our words. will allow us to add and subtract as needed.
pirate = {
'hi':'yo-ho-ho','Hi':'Yo-Ho-Ho',
'my':'me','My':'Me',
'friend':'bucko','Friend':'Bucko',
'sir':'matey','Sir':'Matey',
'where':'whar','Where':'Whar',
'is':'be','Is':'Be',
'the':'th','The':'Th',
'there':'thar','There':'Thar',
'you':'ye','You':'Ye'
}

# created a list of punctuation that we are likely to see.
punctuation = ['.','!',',']

# defining the main function of the program.
def main():
    phrase = input('\nEnter your words bucko! We gonna make a pirate outa ya: ')
    translation = replace(phrase)
    print()
    print(translation)
    play_again()

# this function is the logical steps for the translation from input to pirate talk.
def replace(phrase):
    pirate_talk = []
    punct = ''
    words = phrase.split()
    # broke the string into a list to allow us to iterate over entire words 
    # instead of letters. this prevented partial word replacement such as mistaking there for the.
    for word in words:
        arr = random.randrange(0,6)
        if arr == 1 or arr == 3 or arr == 5:
            pirate_talk.append('arr')
    # i set this so that it weill check each word in case the user enters two sentences or uses puntuation within the input.
        if word[-1] in punctuation: 
            punct = word[-1]
            word = word.replace(word, word[0:-1])
        if word.endswith('ing'):
            word = word.replace('ing','in')
        if word in pirate:
            pirate_talk.append(pirate[word] + punct)
            punct = '' 
            # need to clear the punct after each use or it will continue 
            # to print after the next words even if no new punctuation is present.
        else:
            pirate_talk.append(word + punct)
            punct = ''
    

    pirate_talk = ' '.join(pirate_talk) # used join to turn the list back into a string.
    return pirate_talk
    
def play_again():
    play = input('\nWould you like to play again Matey (Y/N):').lower()
    if play == 'y':
        main()
    else:
        print('\nArr! Scared of Davey Jones locker are ye? Come back when you are ready to talk like pirate!')
    
    
if __name__ == '__main__':
    main()
