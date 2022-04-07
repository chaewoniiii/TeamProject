import requests
import json

TMDB_API_KEY = str('743aacc2c915315a8f9586ae04e0d1fe')

def get_movie_datas():
    total_data = []
    BASE_URL = "https://api.themoviedb.org/3/movie/"

    for i in range(1, 3):
        print("{}번째 진행 중.".format(i))
        request_url = "https://api.themoviedb.org/3/movie/popular?api_key={}&language=ko-kr&page={}".format(TMDB_API_KEY, i)
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'director': '',
                    'actors': [],
                }

                data = {
                    "pk": movie['id'],
                    "model": "movie.movie",
                    "fields": fields
                }

                total_data.append(data)

                for data in total_data:
                    movie_id = data['fields']['movie_id']
        
                    credit_request_url = f"{BASE_URL}{movie_id}/credits?api_key={TMDB_API_KEY}"
                    credit_info = requests.get(credit_request_url).json()

                for cast in credit_info['cast'][:5]:
                    data['fields']['actors'].append(cast['name'])
        
                if credit_info['crew']:
                    data['director'] = credit_info['crew'][0]['name']

                

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()