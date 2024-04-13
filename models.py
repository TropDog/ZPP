class Movies:
    def __init__(self, movie_id: int, title: str, genre: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.genre = genre

class Ratings:
    def __init__(self, user_id: int,movie_id: int, rating: float, timestamp: int) -> None:
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp
    
class Tags:
    def __init__(self, user_id: int,movie_id: int, tag: str,timestamp: int) -> None:
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

class Links:
    def __init__(self, movie_id: int,imdb_id: int, tmdb_id: int) -> None:
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id








