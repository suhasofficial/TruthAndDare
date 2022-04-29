
import random

#---------items of truth or dare--------

truth_items = ['What is your worst habit?', 'Do you sing in the shower?', 'Are you scared of the dark?']
dare_items  = ['dance in the street like crazy.', 'Bark like a dog loudly.', 'take your shirt off spin it.']

#---------------------------------------

number_of_players = input('How many people wants to play?')
number_of_players = int(number_of_players)
list_of_players = []

answer = "yes"

for i in range(number_of_players) :
    player_names = input("please enter player's name.")
    list_of_players.append(player_names)

while answer == "yes" or answer == "y" :

    player = random.choice(list_of_players)
    print('its «', player, '»  turn')

    truth_dare = input('please type "truth" to choose truth and "dare" to choose dare.')

    truth_dare = str(truth_dare)

    if truth_dare == 'truth' :
        print(random.choice(truth_items))


    if truth_dare == 'dare' :
        print(random.choice(dare_items))

    answer = input("Do you wanna continue the game?")