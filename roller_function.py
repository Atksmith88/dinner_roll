from lists import *
import random
from IPython.display import clear_output


def roll():
    while True:
        selection = input("Please enter your 20-sided die roll, or enter 'Roll' to have a number selected for you: ")
        if selection.lower() == 'roll':
            selection = int(random.randint(1, 20))
        else:
            selection = int(selection)
        
        if selection == 2:
            total = []
            for i, lst in main.items():
                if type(lst) == str:
                    total.append(lst)
                else:
                    for item in lst:
                        if item not in total:
                            total.append(item)
            rand_selection = random.randint(0, len(total)-1)
            print('You rolled a 2, which is a random choice from all of them!')
            print(f'Your restaurant for tonight is {total[rand_selection]}, enjoy!')
        elif selection == 1:
            print(f'You rolled a 1, a critical failure! Your restaurant is {main.get(selection)}, good luck!')
        elif selection == 20:
            print(f'You rolled a 20, a critical success! Your restaurant is {main.get(selection)}, congratulations!')
        elif selection == 10:
            print('You rolled a 10, that means you get to go somewhere new! Hope you enjoy it!')
        else:
            cat = list.get(selection)
            num = len(main.get(selection))
            die = 'd6' if num == 6 else 'd4'
            print(f'Your roll was {selection}, which means your category is {cat}! This category has {num} options.')
            new_selection = input(f"Please roll a {die} and enter the number or enter 'Roll' to have a number selected for you: ")
            if new_selection.lower() == 'roll':
                new_selection = int(random.randint(1, num-1))
            else:
                new_selection = int(new_selection)
            print(f'Your roll is {new_selection}, so your restaurant is {main.get(selection)[new_selection]}, enjoy!')
        if input('Start over? y/n: ') == 'y':
            clear_output()
            continue
        else:
            print('Thanks for rolling, enjoy your meal!')
            break