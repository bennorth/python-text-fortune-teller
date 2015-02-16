outside_colours = ['RED', 'GREEN', 'BLUE', 'YELLOW']

def player_choice(name, choices):
    print('choose a ' + name + ':')
    for i in range(0, len(choices)):
        print(choices[i])

    choice = input('--> ')
    return choice

colour_choice = player_choice('colour', outside_colours)
print('you chose ' + colour_choice)

n_letters_in_colour = len(colour_choice)
print(n_letters_in_colour)

# RED (3 letters) and GREEN (5 letters) lead to [1, 2, 5, 6]
# BLUE (4 letters) and YELLOW (6 letters) lead to [3, 4, 7, 8]

if n_letters_in_colour in [3, 5]:
    first_number_choices = ['1', '2', '5', '6']
else:
    first_number_choices = ['3', '4', '7', '8']

first_number_chosen = player_choice('number', first_number_choices)
