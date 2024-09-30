import requests
from bs4 import BeautifulSoup
from ..config import Config
from ..utils.logger import logger

class MovieInfoFetcher:
    def __init__(self):
        self.omdb_api_key = Config.OMDB_API_KEY
        self.tmdb_api_key = Config.TMDB_API_KEY

    def fetch_omdb_info(self, movie_name: str) -> dict:
        url = f"http://www.omdbapi.com/?t={movie_name}&plot=full&apikey={self.omdb_api_key}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}

    def fetch_tmdb_info(self, movie_name: str) -> dict:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={self.tmdb_api_key}&query={movie_name}"
        response = requests.get(search_url)
        if response.status_code == 200:
            results = response.json().get('results', [])
            if results:
                movie_id = results[0]['id']
                details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.tmdb_api_key}&append_to_response=credits"
                details_response = requests.get(details_url)
                return details_response.json() if details_response.status_code == 200 else {}
        return {}

    def fetch_wikipedia_summary(self, movie_name: str) -> str:
        movie_name = movie_name.replace(' ', '_')  # Replace spaces with underscores for Wikipedia
        search_url = f"https://en.wikipedia.org/wiki/{movie_name}_(film)"
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            plot_section = soup.find('span', {'id': 'Plot'})
            if plot_section:
                plot_paragraphs = plot_section.find_next('p').find_next_siblings('p')
                return ' '.join([p.text for p in plot_paragraphs])
        return ""

    def fetch_all(self, movie_name: str) -> dict:
        omdb_info = self.fetch_omdb_info(movie_name)
        tmdb_info = self.fetch_tmdb_info(movie_name)
        wiki_summary = self.fetch_wikipedia_summary(movie_name)

        return {
            'omdb': omdb_info,
            'tmdb': tmdb_info,
            'wikipedia': wiki_summary
        }
