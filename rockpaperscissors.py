from random import *
import random
from time import sleep

stuff = ['rock', 'paper', 'scissors']

yourChoise = str(input('You chose: '))
botChoise = random.choice(stuff)

sleep(1)

print('The bot choose: ' + botChoise)

sleep(1)

#rock combinations

if yourChoise == 'rock' and botChoise == 'rock':
    print('Tie!')
elif yourChoise == 'rock' and botChoise == 'paper':
    print('You lost!')
elif yourChoise == 'rock' and botChoise == 'scissors':
    print('You won!')

#paper combinations

if yourChoise == 'paper' and botChoise == 'paper':
    print('Tie!')
elif yourChoise == 'paper' and botChoise == 'scissors':
    print('You lost!')
elif yourChoise == 'paper' and botChoise == 'rock':
    print('You won!')

#scissors combinations

if yourChoise == 'scissors' and botChoise == 'scissors':
    print('Tie!')
elif yourChoise == 'scissors' and botChoise == 'rock':
    print('You lost!')
elif yourChoise == 'scissors' and botChoise == 'paper':
    print('You won!')

    
    
    
    
    
    #MORANGO!!!
