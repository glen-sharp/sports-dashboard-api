import requests
from xml.etree import ElementTree as ET

class ApiRequests:
    def __init__(self):
        self.last_race_url = 'http://ergast.com/api/f1/current/last/results'
        self.last_race_num = 5

    def get_last_race_data(self):
        response = requests.get(
            self.last_race_url,
            timeout=30000,
        )

        root = ET.fromstring(response.content)
        race_name = root.find('{http://ergast.com/mrd/1.5}RaceTable')\
            .find('{http://ergast.com/mrd/1.5}Race')\
            .find('{http://ergast.com/mrd/1.5}RaceName').text

        results = root.find('{http://ergast.com/mrd/1.5}RaceTable')\
            .find('{http://ergast.com/mrd/1.5}Race')\
            .find('{http://ergast.com/mrd/1.5}ResultsList')\
            .findall('{http://ergast.com/mrd/1.5}Result')

        results_dict = []

        for result in results:

            driver = result.find('{http://ergast.com/mrd/1.5}Driver')
            forename = driver.find('{http://ergast.com/mrd/1.5}GivenName').text
            surname = driver.find('{http://ergast.com/mrd/1.5}FamilyName').text

            if result.find('{http://ergast.com/mrd/1.5}Time') is None:
                time = None
            else:
                time = result.find('{http://ergast.com/mrd/1.5}Time').text

            results_dict.append({
                'position': result.attrib['position'],
                'name': f'{forename} {surname}',
                'time': time,
                'points': result.attrib['points'],
            })

        return race_name, results_dict
