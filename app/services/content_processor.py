import re
from ..utils.logger import logger

class ContentProcessor:
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove citations
        text = re.sub(r'\[\d+\]', '', text)
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    @staticmethod
    def combine_info(movie_info: dict) -> str:
        combined_text = ""

        # Add movie metadata
        if movie_info['omdb']:
            combined_text += f"Title: {movie_info['omdb'].get('Title', '')}\n"
            combined_text += f"Year: {movie_info['omdb'].get('Year', '')}\n"
            combined_text += f"Director: {movie_info['omdb'].get('Director', '')}\n"
            combined_text += f"Genre: {movie_info['omdb'].get('Genre', '')}\n\n"

        # Combine plot information
        plot_info = []
        if movie_info['omdb'] and movie_info['omdb'].get('Plot'):
            plot_info.append(movie_info['omdb']['Plot'])
        if movie_info['tmdb'] and movie_info['tmdb'].get('overview'):
            plot_info.append(movie_info['tmdb']['overview'])
        if movie_info['wikipedia']:
            plot_info.append(movie_info['wikipedia'])

        combined_text += "Plot Summary:\n\n" + "\n\n".join(plot_info)

        return ContentProcessor.clean_text(combined_text)
