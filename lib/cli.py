#!/usr/bin/env python3

from db.models import Grape, Bottle, Winery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.value =  user_input
        CLI.start(self)

    def start(self):
        print('***** Welcome To The Virtual Wine Keeper *****')
        exit = False
        while exit == False:
            user_input = input("Would you like to stop now? (Type Y/N): ")
            if user_input == "Y" or user_input == 'y':
                exit = True

            else:
                user_action = input("Type B to add a bottle, G to add a grape or W to add a winery: ")
                if user_action == "G" or user_action == "g":
                    grape_name = input("Type grape name: ")
                    grape = Grape(name = grape_name)

                    session.add(grape)
                    session.commit()


        
def printer(user_input):
    print(f'Goodbye {user_input}!')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    my_object = CLI(user_input)
    print(printer(my_object.value))