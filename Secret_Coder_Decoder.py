# Name: Secret Coder
# Date: April 24, 2021
# Purpose: This program encodes / decodes a users message. 
# For fun I built this using an easy key:value pattern and a single key password. 
# If desired, we could add a secondary key or increase the mathmatical 
# complexity to add increased security.

# numerical key for encoding / decoding
pwd = int

# key:values for encoding / decoding
secrete_code = {
' ':0, 'a':1, 'b':3, 'c':2,
'd':4, 'e':6, 'f':5, 'g':7, 'h':9,
'i':8, 'j':10, 'k':12, 'l':11,
'm':13, 'n':15, 'o':14, 'p':16, 'q':18,
'r':17, 's':19, 't':21, 'u':20,
'v':22, 'w':24, 'x':23, 'y':25, 'z':26
}

# defining the main function of the program.
def main():
    global pwd
    print('Welcome to the Super Secret Coder.\n')
    task = input('Enter 1 to encode\nEnter 2 to decode: ')
    # take the user input and call on the appropriate function.
    # if the input produces an error, user informed and asked if they want to try again.
    try:
        if task == '1':
            phrase = input('Enter your secret code: ').lower()
            pwd = int(input('Enter a key bewteen 1-5: '))
            encoded = encode(phrase)
            print(f'Secret Code: {encoded}')
        elif task == '2':
            phrase = input('Enter your secret code: ')
            pwd = int(input('Enter your key number: '))
            decoded = decode(phrase)
            print(f'Secret Message: {decoded}') 
    except:
        print('That is not a recognized input.')
    play_again()

# logical steps for encoding.
def encode(phrase):
    phrase = list(phrase)
    encoded = []
    for char in phrase:
        encoded.append(str(secrete_code[char]*pwd))
    
    encoded = '-'.join(encoded) # used join to turn the list back into a string with hyphen seperators.
    return encoded 

# logical steps for decoding.
def decode(phrase):
    phrase = phrase.split('-')
    decoded = []
    for num in phrase:
        num = int(num)
        num = num / pwd
        for key, value in secrete_code.items(): # this allows us to determine the key based on the value.
            if num == value:
                decoded.append(key)
    decoded = ''.join(decoded) # used join to turn the list back into a string.
    return decoded

def play_again():
    play = input('\nWould you like to encode or decode again (Y/N):').lower()
    if play == 'y':
        main()
    else:
        input('\nRemember to keep secure with Super Secure Coder.\n')

if __name__ == '__main__':
    main()
