from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseScraper(ABC):
    """
    Abstract base interface for ticket platform scrapers / API fetchers.
    """
    
    @abstractmethod
    def search_movies(self, city: str, query: str = "") -> List[Dict[str, Any]]:
        """
        Search currently listed or upcoming movies in a given city.
        Returns: list of dicts with keys: name, code, poster_url, release_date
        """
        pass

    @abstractmethod
    def search_theaters(self, city: str, query: str = "") -> List[Dict[str, Any]]:
        """
        Search theaters / venues in a given city.
        Returns: list of dicts with keys: name, venue_code, address
        """
        pass

    @abstractmethod
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
        """
        Fetch showtimes for a specific movie + theater + date.
        Returns: list of dicts with keys:
          - show_id
          - platform
          - movie_name
          - theater_name
          - show_time (e.g. '10:30 AM')
          - format_type (e.g. 'IMAX 2D', '2D', '3D', '4DX')
          - price_info (e.g. '₹250 - ₹500')
          - status ('AVAILABLE', 'FILLING_FAST', 'SOLD_OUT')
          - booking_url
        """
        pass
