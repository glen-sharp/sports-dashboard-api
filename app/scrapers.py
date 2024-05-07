import requests
from bs4 import BeautifulSoup


class Scrapers:
    """
    Class containing functions to scrape data from
    various URLs
    """
    def __init__(self):
        self.f1_driver_standings_url = 'https://www.gpfans.com/en/f1-standings/2024/'
        self.snooker_rankings_url = 'https://www.snooker.org/res/index.asp?template=35'

    def get_f1_driver_standings(self):
        """
        Scrapes data from site for F1 driver standings
        """
        page = requests.get(self.f1_driver_standings_url, timeout=30000)
        soup = BeautifulSoup(page.content, 'html.parser')

        name_results = soup.find_all(class_='names standings-coureur--names')
        name_array = [x.text.strip() for x in name_results]

        points_results = soup.find_all(class_='pnt')
        points_array = [x.text.strip() for x in points_results]

        driver_list = []

        for i, name in enumerate(name_array):
            driver_list.append({
                'ranking': i + 1,
                'name': name,
                'points': int(points_array[i]),
            })

        return driver_list

    def get_snooker_player_rankings(self):
        """
        Scrapes data from side for snooker player rankings
        """
        page = requests.get(self.snooker_rankings_url, timeout=30000)
        soup = BeautifulSoup(page.content, 'html.parser')

        players = soup.find_all(class_='gradeA')

        player_list = []

        for i, player in enumerate(players[:20]):
            player_list.append({
                'ranking': i + 1,
                'name': player.find(class_='player').text,
                'nationality': player.find(class_='nationality').text,
                'sum': int(player.find(class_='sum').text),
            })

        return player_list
