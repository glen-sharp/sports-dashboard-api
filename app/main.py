from fastapi import FastAPI

from scrapers import Scrapers
from api_client import ApiRequests

app = FastAPI()

@app.get('/f1_driver_standings')
async def root():
    """
    Endpoint to return F1 driver standings
    """
    scraper = Scrapers()
    data = scraper.get_f1_driver_standings()

    return {'driver_standing_array': data}

@app.get('/f1_latest_race')
async def root():
    """
    Endpoint to return data for last F1 race
    """
    api_client = ApiRequests()

    race_name, data = api_client.get_last_race_data()

    return {
        'race_name': race_name,
        'last_race_standings': data,
    }

@app.get('/snooker_rankings')
async def root():
    """
    Endpoint to return current snooker player rankings
    """
    scraper = Scrapers()

    data = scraper.get_snooker_player_rankings()

    return {
        'snooker_player_rankings': data,
    }
