
from os import name, system
from info_finder import Finder
from data import *
from system import System
from make_table import MakeTable
system = System()
program_in_progress = True

while program_in_progress == True:
    print(logo)
    regions = input('Please enter a region: ')
    player = input('\nPlease enter a username: ')
    if regions not in region:
        system.clear_terminal()
        print(f"You entered '{regions}' ------ It's invalid region\n")
        print("Press enter to reset program")
        system.pause()
        system.restart_program()
        

    info = Finder(regions,player)
   
    if info.rank()== False or info.league_points()== False or info.level()== False or info.winrate() == False:
        system.clear_terminal()
        print(f"The {player} doesn't exsist\n")
        answers = input("Do you want to reset the program(type 'yes' or 'no'): ")
        if answers == 'yes':
            system.restart_program()
        else:
            system.exit_app()
    else:
        system.clear_terminal()
        rank = info.rank()
        league_points = info.league_points()
        level = info.level()
        winrate = info.winrate()
        table = MakeTable()
        table.make_table(regions,player,rank, league_points,  level, winrate)
        answers = input("\nDo you want to reset the program(type 'yes' or 'no'): ")
        if answers == 'yes':
            system.restart_program()
        else:
            system.exit_app()
        
