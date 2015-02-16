outside_colours = ['RED', 'GREEN', 'BLUE', 'YELLOW']

def player_choice(name, choices):
    print('choose a ' + name + ':')
    for i in range(0, len(choices)):
        print(choices[i])

    choice = input('--> ')
    return choice

colour_choice = player_choice('colour', outside_colours)
print('you chose ' + colour_choice)
