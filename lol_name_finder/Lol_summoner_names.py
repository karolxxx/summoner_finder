#imports
import bs4, requests
import os
from logo import logo
import sys

def main():
    #Find summoner winrate
    def restart_program():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('The username doesnt exsist')
        restart_program = input('\nDo you want to restart the program("y" or "n"):\n')
        if restart_program == 'y':
             os.system('cls' if os.name == 'nt' else 'clear')
             os.system('python "C:\\Users\\Kamis\\Desktop\\lol_name_finder\\Lol_summoner_names.py"')
        else:
            print('Press enter to exit program')
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit(0)




    def summoner_winrate(region, player_name):
        if region == 'kr':
            res = requests.get('https://.op.gg/summoner/userName='+player_name)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio')
            if elem == []:
                restart_program()
            else:
                winrate = elem[0].text.strip()
                return winrate 
        else:
            res = requests.get('https://'+region+'.op.gg/summoner/userName='+player_name)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio')
            if elem == []:
                restart_program()
            else:
                winrate = elem[0].text.strip()
                return winrate
        
    #Finds summoner rank 
    def summoner_rank(region,player_name):
        if region == 'kr':
            res = requests.get('https://'+region+'.op.gg/summoner/userName='+player_name)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
            if elem == []:
                restart_program()
            else:
                rank = elem[0].text.strip()
                return rank

        else:
            res = requests.get('https://'+region+'.op.gg/summoner/userName='+player_name)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
            if elem == []:
                restart_program()
            else:
                rank = elem[0].text.strip()
                return rank
    #main info  
    list_regions = ['eune', 'lan', 'euw', 'jp','oce', 'br', 'las', 'ru', 'tr', 'kr','na' ]
    end_program = False
    
    # Loop
    while end_program == False:
        #checks the region
        print(logo)
        region = input('\nEnter a region:\n').lower()
        if region not in list_regions:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('You entered a wrong region')
            print('The program will restart')
            os.system("PAUSE")
            os.system('cls' if os.name == 'nt' else 'clear') 
            os.system('python "C:\\Users\\Kamis\\Desktop\\lol_name_finder\\Lol_summoner_names.py"')
        player_name = input('\nEnter a player name:\n')
        
        #runs the function
        winrate = summoner_winrate(region, player_name)   
        rank = summoner_rank(region,player_name)
        os.system('cls' if os.name == 'nt' else 'clear')

        #output
        print(f'{player_name} is from {region} has '+winrate)
        print(f'\nHe is {rank} rank\n')
        os.system("pause")
        
        #ask if the user wants to stop the loop
        again = input("Do you want to search another player (type 'y' or 'n'):\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        if again == 'n':
            end_program = True
            break

main()