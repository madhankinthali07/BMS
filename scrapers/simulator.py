import random
from typing import List, Dict, Any, Optional
from scrapers.base import BaseScraper

class SimulatorScraper(BaseScraper):
    """
    Simulated scraper engine for testing and demonstration.
    Allows testing immediate show opening and new show additions.
    """

    SAMPLE_TIMES = ["09:30 AM", "01:15 PM", "04:45 PM", "07:30 PM", "10:15 PM", "11:45 PM"]
    SAMPLE_FORMATS = ["IMAX 2D", "IMAX 3D", "4DX", "Dolby Atmos 2D", "2D"]

    def search_movies(self, city: str, query: str = "") -> List[Dict[str, Any]]:
        return [
            {"name": "Avatar: Fire and Ash (Demo)", "code": "SIM_AVATAR", "poster_url": "", "release_date": "Demo"},
            {"name": "Dune: Part Two (Demo)", "code": "SIM_DUNE", "poster_url": "", "release_date": "Demo"},
            {"name": "Pushpa 2: The Rule (Demo)", "code": "SIM_PUSHPA", "poster_url": "", "release_date": "Demo"}
        ]

    def search_theaters(self, city: str, query: str = "") -> List[Dict[str, Any]]:
        return [
            {"name": f"PVR IMAX Palladium, {city.title()}", "venue_code": "SIM_PVR", "address": f"Grand Mall, {city.title()}"},
            {"name": f"INOX Megaplex, {city.title()}", "venue_code": "SIM_INX", "address": f"City Center, {city.title()}"}
        ]

    def fetch_shows(
        self,
        city: str,
        movie_name: str,
        movie_code: Optional[str],
        theater_name: str,
        venue_code: Optional[str],
        target_date: str,
        format_filter: Optional[str] = "ALL"
    ) -> List[Dict[str, Any]]:
        # Returns simulated active shows
        selected_times = random.sample(self.SAMPLE_TIMES, k=random.randint(2, 4))
        shows = []
        actual_movie = movie_name
        if not actual_movie or "ANY" in actual_movie.upper() or "ALL" in actual_movie.upper():
            actual_movie = "Pushpa 2: The Rule (Demo)"
        for idx, t in enumerate(selected_times):
            fmt = "IMAX 2D" if (format_filter and "IMAX" in format_filter.upper()) else random.choice(self.SAMPLE_FORMATS)
            shows.append({
                "show_id": f"sim_{idx}_{t.replace(' ', '_')}",
                "platform": "BookMyShow (Simulated)",
                "movie_name": actual_movie,
                "theater_name": theater_name,
                "show_time": t,
                "format_type": fmt,
                "price_info": "₹350 - ₹650",
                "status": "AVAILABLE",
                "booking_url": "https://in.bookmyshow.com"
            })
        return shows
