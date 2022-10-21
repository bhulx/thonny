#hangman 3


import random
_dict = {0: 'cyclone', 1: 'package', 2: 'beagles', 3: 'trinity', 4: 'vassels', 5: 'flowers'}
#wds_ = ['cyclone','package', 'beagle']

def generate():
    num_ = random.randint(0,5)
    return _dict[num_]
word = generate()

print(word)

display = []
wrd_lgt = len(word)
print(wrd_lgt)
      
for i in range(wrd_lgt):
    display += '_'
print(display)
hangman = 6
gs = ''
#letter = ''
while hangman >0:    
    gs = input('enter a letter \n', )
    if gs not in word:
        hangman = hangman - 1
        print("wrong, you have", hangman, 'lives left')
        if hangman == 0:
            print("YOU are DEAD")
            break
    else:
        #print(hangman)
        if word[0]  == gs:
            display[0] = gs
        if word[1]  == gs:
            display[1] = gs
        if word[2]  == gs:
            display[2] = gs
        if word[3]  == gs:
            display[3] = gs
        if word[4]  == gs:
            display[4] = gs
        if word[5]  == gs:
            display[5] = gs
        if word[6]  == gs:
            display[6] = gs
        print(display)
        guess_ = ''
        sep_string = ''
        print(sep_string.join(display))
        guess_ = display
        print(guess_)
        if str(guess_) == str(word):
            print("YOU WIN ")
            break
print('thank you for playing') 
    
    
    




                  
























