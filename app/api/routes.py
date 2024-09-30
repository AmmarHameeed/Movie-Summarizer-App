from fastapi import APIRouter, HTTPException
from urllib.parse import quote
from ..services.movie_info_fetcher import MovieInfoFetcher
from ..services.content_processor import ContentProcessor
from ..services.summarizer import Summarizer
from ..utils.logger import logger

router = APIRouter()
movie_info_fetcher = MovieInfoFetcher()
content_processor = ContentProcessor()
summarizer = Summarizer()

@router.get("/summarize/{movie_name}")
async def summarize_movie(movie_name: str):
    try:
        movie_name = quote(movie_name)  # URL-encode the movie name
        movie_info = movie_info_fetcher.fetch_all(movie_name)
        combined_content = content_processor.combine_info(movie_info)
        summary = summarizer.summarize(combined_content)

        return {
            "movie": movie_name,
            "summary": summary,
            "word_count": len(summary.split()),
            "year": movie_info['omdb'].get('Year', 'N/A'),
            "director": movie_info['omdb'].get('Director', 'N/A'),
            "genre": movie_info['omdb'].get('Genre', 'N/A')
        }
    except Exception as e:
        logger.error(f"Error summarizing movie {movie_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred while summarizing the movie: {str(e)}")
