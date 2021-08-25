import bs4, requests

class Finder:

    def __init__(self, regions,player ):
        super().__init__()
        self.region = regions
        self.username = player


    def winrate(self,):
        if self.region == 'kr':
            res = requests.get('https://.op.gg/summoner/userName='+self.username)
        else:
            res = requests.get('https://'+self.region+'.op.gg/summoner/userName='+self.username)   
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio')
        if elem == []:
            return False
        else:
          winrate = elem[0].text
          return winrate

    def level(self):
        if self.region == 'kr':
            res = requests.get('https://.op.gg/summoner/userName='+self.username)
        else:
            res = requests.get('https://'+self.region+'.op.gg/summoner/userName='+self.username)   
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elem = soup.select('body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Face > div > span')
        if elem == []:
            return False
        else:
          level = elem[0].text
          return level
    
    def rank(self):
        if self.region == 'kr':
            res = requests.get('https://.op.gg/summoner/userName='+self.username)
        else:
            res = requests.get('https://'+self.region+'.op.gg/summoner/userName='+self.username)   
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
        if elem == []:
            return False
        else:
          rank = elem[0].text
          return rank
    
    def league_points(self):
       if self.region == 'kr':
            res = requests.get('https://.op.gg/summoner/userName='+self.username)
       else:
            res = requests.get('https://'+self.region+'.op.gg/summoner/userName='+self.username)   
       res.raise_for_status()
       soup = bs4.BeautifulSoup(res.text, 'html.parser')
       elem = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.LeaguePoints')
       if elem == []:
          return False
       else:
          lp = elem[0].text.strip()
          return lp 
