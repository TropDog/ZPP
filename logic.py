from models import Movies, Ratings, Tags, Links

def read_csv(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        return data

def read_movies(path: str):
    data = read_csv(path)
    list_of_movies = []

    for movie in data:
        if len(movie.split(',')) == 3:
            movie_id, title, genre = movie.split(',')
            m1 = Movies(movie_id, title, genre)
            list_of_movies.append(m1)
    
    return list_of_movies

def read_ratings(path: str):
    data = read_csv(path)
    list_of_ratings = []

    for rating in data:
        if len(rating.split(',')) == 4:
            user_id, movie_id, rating, timestamp = rating.split(',')
            r1 = Ratings(user_id, movie_id, rating, timestamp)
            list_of_ratings.append(r1)
    
    return list_of_ratings

def read_tags(path: str):
    data = read_csv(path)
    list_of_tags = []

    for tag in data:
        if len(tag.split(',')) == 4:
            user_id, movie_id, tag, timestamp = tag.split(',')
            t1 = Tags(user_id, movie_id, tag, timestamp)
            list_of_tags.append(t1)
    
    return list_of_tags

def read_links(path: str):
    data = read_csv(path)
    list_of_links = []

    for link in data:
        if len(link.split(',')) == 3:
            movie_id, imdb_id, tmdb_id = link.split(',')
            l1 = Links(movie_id, imdb_id, tmdb_id)
            list_of_links.append(l1)
    
    return list_of_links

def serialized_data(file_name: str):
    path = file_name + '.csv'
    match file_name:
        case 'movies':
            list = read_movies(path)
        case 'ratings':
            list = read_ratings(path)
        case 'tags':
            list = read_tags(path)
        case 'links':
            list = read_links(path)
            
    json_list = []

    for object in list:
        json_list.append(object.__dict__)
    return json_list[1:]





