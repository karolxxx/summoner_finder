#imports
import bs4, requests
import os
from logo import logo

#main function
def summoner_name_finder(region, player_name):
    res = requests.get('https://'+region+'.op.gg/summoner/userName='+player_name)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio')
    return elem[0].text.strip()

def summoner_rank(region,player_name):
    res = requests.get('https://'+region+'.op.gg/summoner/userName='+player_name)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
    return elem[0].text.strip()

#inputs
print(logo)
region = input('\nEnter a region:\n').lower()
player_name = input('Enter a summoner name:\n')

#runs the function
winrate = summoner_name_finder(region, player_name)
rank = summoner_rank(region,player_name)
os.system('cls' if os.name == 'nt' else 'clear')
print(f'{player_name} is from {region} has '+winrate)
print(f'He is {rank} rank')
os.system("pause")




