from scrapers.base import BaseScraper
from scrapers.bookmyshow import BookMyShowScraper
from scrapers.district import DistrictScraper
from scrapers.simulator import SimulatorScraper

bms_scraper = BookMyShowScraper()
district_scraper = DistrictScraper()
simulator_scraper = SimulatorScraper()

def get_scraper_for_platform(platform: str) -> BaseScraper:
    p = platform.lower()
    if "district" in p:
        return district_scraper
    elif "sim" in p:
        return simulator_scraper
    return bms_scraper
