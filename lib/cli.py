#!/usr/bin/env python3

from db.models import Grape, Bottle, Winery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

class CLI:
    def __init__(self, user_input):
        self.grapes = [grape for grape in session.query(Grape)]
        self.wineries = [winery for winery in session.query(Winery)]
        self.bottles = [bottle for bottle in session.query(Bottle)]
        self.name = user_input
        self.start()

    def start(self):
        print(' ')
        print(f'***** Welcome To The Virtual Wine Keeper {self.name} *****')
        print(' ')

        exit_loop = False
        while exit_loop == False:
                choice = input(f'Type "list" to see the wineries, bottles or grapes, type "add" to add a bottle, winery or grape, type "search" to find bottles by winery or grape, type "exit" to end session: ')
                print(' ') 
                if choice.lower() == "list":
                     show_data(self)
                elif choice.lower() == "add":
                     add_data(self)
                elif choice.lower() == "search":
                     search_data(self)
                elif choice.lower() == "exit":
                    exit_loop = True
                else:
                    print_error(self.name)

        print_goodbye(self.name)

def add_data(self):
    user_action = prompt_bgw()

    while user_action != "B" and user_action != "b" and user_action != "G" and user_action != "g" and user_action != "W" and user_action != "w":
        print_error(self.name)
        user_action = prompt_bgw()

    if user_action == "G" or user_action == "g":
        name = input("Type grape name: ")
        grape = Grape(name = name)

        session.add(grape)
        session.commit()

        self.grapes.append(grape)

    elif user_action == "W" or user_action == "w":
        name = input("Type winery name: ")
        winery = Winery(name = name)

        session.add(winery)
        session.commit()

        self.wineries.append(winery)

    elif user_action == "B" or "b":
        print_grapes(self.grapes)
        print_wineries(self.wineries)
        print(' ')
        user_input = prompt_gw()
        print(' ')

        while user_input != "Y" and user_input != "y":
            add_data(self)
            print(' ')
            print_grapes(self.grapes)
            print_wineries(self.wineries)
            print(' ')
            user_input = prompt_gw()
            print(' ')

        make_bottle(self)

def make_bottle(self):
    user_grape = input("Type the number of the grape from the list above: ")
    user_winery = input("Type the number of the winery from the list above: ")
    year = input("What vintage is the bottle?: " )
    y = re.compile('[0-9]')
    yr = y.findall(year)

    while len(yr) != 2 and len(yr) != 4:
        print(' ')
        print_error(self.name)       
        year = input("What vintage is the bottle?: " )
        y = re.compile('[0-9]')
        yr = y.findall(year)

    price = input("How much did you pay for the bottle?: " )
    p = re.compile('[0-9.]')
    px = p.findall(price)

    while len(px) == 0:
        print(' ')
        print_error(self.name)
        price = input("How much did you pay for the bottle?: " )
        p = re.compile('[0-9.]')
        px = p.findall(price)

    px = ''.join(px)

    score = input("How would you rate it on a scale of 1-10?: " )
    while not score or int(score) <1 or int(score) >10:
        print(' ')
        print_error(self.name)
        score = input("How would you rate it on a scale of 1-10?: " )

    bottle = Bottle(
            price = px,
            score = score,
            year = year,
            grape_id = self.grapes[int(user_grape) - 1].id,
            winery_id = self.wineries[int(user_winery) - 1].id
    )

    session.add(bottle)
    session.commit()

    self.bottles.append(bottle)
    print(' ')
    print('Congratulations! You have added the following wine to your Vitual Cellar!')

    print_bottle(bottle)

def search_data(self):
    user_action = input("Type G to search bottles by grape or W to search bottles by winery: ")
    print(' ')
    
    while user_action != "G" and user_action != "g" and user_action != "W" and user_action != "w":
        print_error(self.name)
        user_action = input("Type G to search bottles by grape or W to search bottles by winery: ")
        print(' ')

    if user_action == "G" or user_action == "g":
        print_grapes(self.grapes)
        valid_pick = False
        while not valid_pick:
            user_pick = input("Type the number of the grape from the list above to see bottles of that grape: ")
            if int(user_pick) in range(1, len(self.grapes)):
                valid_pick = True
            else:
                print(' ')
                print_error(self.name)
                
        print(' ')
        print_bottles(self.grapes[int(user_pick) - 1].bottles)
        
    elif user_action == "W" or user_action == "w":
        print_wineries(self.wineries)
        valid_pick = False
        while not valid_pick:
            user_pick = input("Type the number of the winery from the list above to see bottles from that winery: ")
            if int(user_pick) in range(1, len(self.bottles)):
                valid_pick = True
            else:
                print(' ')
                print_error(self.name)

        print(' ')
        print_bottles(self.wineries[int(user_pick) - 1].bottles)

def show_data(self):
    user_action = input("Type B to list your bottles, G to list grapes or W to list wineries: ")
    print(' ')
    if user_action == "G" or user_action == "g":
        print_grapes(self.grapes)
    elif user_action == "W" or user_action == "w":
        print_wineries(self.wineries)
    elif user_action == "B" or user_action == "b":
        print_bottles(self.bottles)

def print_grapes(grapes):
    print(' ')
    print('** Grapes **')
    print(' ')

    for index, grape in enumerate(grapes):
        print(f'{index + 1}. {grape.name}')

    print(' ')

def print_wineries(wineries):
    print(' ')
    print('** Wineries **')
    print(' ')

    for index, winery in enumerate(wineries):
        print(f'{index + 1}. {winery.name}')
    
    print(' ')

def print_bottles(bottles):
    print(' ')
    print('** Bottles **')
    print(' ')

    for index, bottle in enumerate(bottles):
        print_bottle(bottle)
    print(' ')   

def print_bottle(bottle):
    print(' ')
    print(f'Winery: {bottle.winery.name}')
    print(f'Grape: {bottle.grape.name}')
    print(f'    Year:  {bottle.year}')
    print(f'    Price: ${round(bottle.price, 2)}')
    print(f'    Score: {bottle.score}')
        
def print_goodbye(name):
    print(' ')
    print(f'Goodbye {name}!')

def prompt_bgw():
    user_action = input("Type B to add a bottle, G to add a grape or W to add a winery: ")
    print(' ')
    return user_action

def prompt_gw():
    user_action = input("Is your Grape and Winery in the lists above? (Type Y/N): ")
    print(' ')
    return user_action

def print_error(name):
        print(f'Sorry {name}, but I am not sure what you mean.  Please try that again.')
        print(' ')

import click

@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Hello {name}!")
    CLI(name)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    hello()

 