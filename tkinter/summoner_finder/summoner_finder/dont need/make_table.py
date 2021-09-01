from os import name
from prettytable import PrettyTable

class MakeTable():
    def __init__(self,):
        self.table = PrettyTable()
        
       

    def make_table(self,regions,player,rank, league_points,  level, winrate):
         self.table.field_names = ['summoner','level', 'rank','lp','winrate', 'region']
         self.table.add_row([player, level, rank, league_points, winrate, regions  ])
         print(self.table)