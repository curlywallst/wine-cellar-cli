#!/usr/bin/env python3

from db.models import Grape, Bottle, Winery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.value =  user_input
        CLI.start(self)

    def start(self):
        print(f'***** Welcome To The Virtual Wine Keeper {self.value} *****')
        exit = False
        while exit == False:

                user_action = input("Type B to add a bottle, G to add a grape or W to add a winery: ")
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

                user_input = input("Would you like to stop now? (Type Y/N): ")
                if user_input == "Y" or user_input == 'y':
                    exit = True


        
def printer(user_input):
    print(f'Goodbye {user_input}!')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    my_object = CLI(user_input)
    print(printer(my_object.value))