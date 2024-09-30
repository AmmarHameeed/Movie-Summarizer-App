# Movie Summarizer App

## Overview

The Movie Summarizer App is a FastAPI application that provides concise summaries of movies. By leveraging multiple data sources, including OMDb, TMDb, and Wikipedia, the API generates high-quality summaries that capture the essence of each film. This application is designed for users and movie enthusiasts who want quick access to movie's plot and summaries.

## Features

- **Multi-Source Data Fetching**: Retrieves movie information from OMDb, TMDb, and Wikipedia.
- **Extractive and Abstractive Summarization**: Combines extractive summarization techniques with advanced abstractive models to generate coherent and relevant summaries.
- **Metadata Inclusion**: Provides additional movie details such as title, year, director, and genre alongside the summary.
- **Post-Processing**: Cleans up the generated summaries to remove irrelevant details and ensure clarity.

## Technologies Used

- Python
- FastAPI
- Transformers (Hugging Face)
- scikit-learn
- BeautifulSoup
- Requests

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movie_summarizer.git
   cd movie_summarizer
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OMDB_API_KEY=your_omdb_api_key
   TMDB_API_KEY=your_tmdb_api_key
   ```

6. **Run the Application**:
   ```bash
   python run.py
   ```

7. **Access the API**:
   Open your web browser and navigate to `http://localhost:8000`. You can also access the API documentation at `http://localhost:8000/docs`.

## API Endpoints

- **GET /summarize/{movie_name}**: Returns a summary of the specified movie.
  - **Parameters**: 
    - `movie_name`: The name of the movie (can include spaces, dashes, or underscores).
  - **Response**: 
    - A JSON object containing the movie title, summary, word count, year, director, and genre.

## Example Request

To get a summary of "The Godfather", you can use the following URL:
```
GET http://localhost:8000/summarize/The%20Godfather
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OMDb API](http://www.omdbapi.com/)
- [TMDb API](https://www.themoviedb.org/documentation/api)


# Instructions to Use
1. Replace yourusername in the clone URL with your actual GitHub username.
2. Replace your_omdb_api_key and your_tmdb_api_key with your actual API keys in the .env section.
3. You can add any additional sections or modify the content as needed to better fit your project.