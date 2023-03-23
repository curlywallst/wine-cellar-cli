#!/usr/bin/env python3

from db.models import Grape, Bottle, Winery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.value =  user_input
        CLI.start(self)

    def start(self):
        print(' ')
        print(f'***** Welcome To The Virtual Wine Keeper {self.value} *****')
        print(' ')
        print('Here are your current bottles: ')
        print(' ')
        print_bottles()
        print(' ')

        exit = False
        while exit == False:
                choice = input(f'Type "list" to see the wineries, bottles or grapes, type "add" to add a bottle, winery or grape, type "search" to find bottles by winery or grape: ')
                print(' ') 
                if choice.lower() == "list":
                     show_data()
                elif choice.lower() == "add":
                     add_data()
                elif choice.lower() == "search":
                     pass
        
                print(' ')
                user_input = input("Would you like to stop now? (Type Y/N): ")
                if user_input == "Y" or user_input == 'y':
                    exit = True

        printer(self.value)

def add_data():
        user_action = input("Type B to add a bottle, G to add a grape or W to add a winery: ")
        print(' ')

        if user_action == "G" or user_action == "g":
            name = input("Type grape name: ")
            grape = Grape(name = name)

            session.add(grape)
            session.commit()

        elif user_action == "W" or user_action == "w":
            name = input("Type winery name: ")
            winery = Winery(name = name)

            session.add(winery)
            session.commit()

        elif user_action == "B" or "b":
            grapes = [grape for grape in session.query(Grape)]
            wineries = [winery for winery in session.query(Winery)]

            print_grapes(grapes)
            print_wineries(wineries)
            print(' ')
            user_input = input("Is your Grape and Winery in the lists above? (Type Y/N): ")
            print(' ')
            if user_input == "Y" or user_input == 'y':
                    
                    user_grape = input("Type the number of the grape from the list above: ")
                    user_winery = input("Type the number of the winery from the list above: ")
                    price = input("How much did you pay for the bottle?: " )
                    score = input("How would you rate it on a scale of 1-10?: " )

                    bottle = Bottle(
                            price = price,
                            score = score,
                            grape_id = grapes[int(user_grape) - 1].id,
                            winery_id = wineries[int(user_winery) - 1].id
                    )

                    session.add(bottle)
                    session.commit()

                    print('Congratulations! You have added the following wine to your Vitual Cellar!')

                    print_bottle(bottle)

def show_data():
    user_action = input("Type B to list bottles, G to list grapes or W to list wineries: ")
    print(' ')
    if user_action == "G" or user_action == "g":
        print_grapes()
    elif user_action == "W" or user_action == "w":
        print_wineries()
    elif user_action == "B" or user_action == "b":
        print_bottles()

def print_grapes(grapes):
    print(' ')
    print('** Grapes **')
    print(' ')

    for index, grape in enumerate(grapes):
        print(f'{index + 1}. {grape.name}')

def print_wineries(wineries):
    print(' ')
    print('** Wineries **')
    print(' ')

    for index, winery in enumerate(wineries):
        print(f'{index + 1}. {winery.name}')

def print_bottles():
    bottles = [bottle for bottle in session.query(Bottle)]
    for index, bottle in enumerate(bottles):
        print_bottle(bottle)
    print(' ')   

def print_bottle(bottle):
    print(' ')
    print(f'Winery: {bottle.winery.name}')
    print(f'Grape: {bottle.grape.name}')
    print(f'    Price: {bottle.price}')
    print(f'    Score: {bottle.score}')
        
def printer(user_input):
    print(' ')
    print(f'Goodbye {user_input}!')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)
