outside_colours = ['RED', 'GREEN', 'BLUE', 'YELLOW']

print('choose a colour:')
for i in range(0, len(outside_colours)):
    print(outside_colours[i])

colour_choice = input('--> ')
print('you chose ' + colour_choice)
