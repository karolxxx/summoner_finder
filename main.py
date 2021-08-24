
from info_finder import Finder
from data import logo
program_in_progress = True

while program_in_progress == True:
    print(logo)
    regions = input('Please enter a region: ')
    player = input('Please enter a username: ')
    info = Finder(regions,player)
   
    if info.rank or info.league_points or info.level or info.winrate == False:
        pass
