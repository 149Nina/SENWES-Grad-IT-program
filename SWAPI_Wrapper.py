import flask
from requests import get
from functools import wraps
from datetime import datetime, timedelta

#create a Flask web application instance.
app = Flask(__name__)

# Use a cache dictionary to keep track of answers and when they expire.
cache = {}

# Function to check if a cached response is still valid
def is_cache_valid(cache_time):
    if cache_time in cache:
        expire_time = cache[cache_time]['expiration_time']
        return datetime.now() < expire_time
    return False

# Decorator function to cache responses for a specified time period
def cache_response_time(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_time = f"{request.path}{str(request.args)}"
            if is_cache_valid(cache_time):
                return cache[cache_key]['response']
            else:
                response = func(*args, **kwargs)
                cache[cache_time] = {
                    'response': response,
                    'expiration_time': datetime.now() + timedelta(seconds=seconds)
                }
                return response
        return wrapper
    return decorator

# Helper function to make API requests to SWAPI
def fetch_SWAPI(url)
    response = get(url)
    return response.json()


#Endpoint for retrieving Star Wars films
@app.route('/films', methods = ['GET'])
@cache_response_time(seconds=300) #cahche for 5 minutes

def get_SW_films():
    swapi_url = 'https://swapi.dev/api/films/'
    films = fetch_SWAPI(swapi_url)
    return jsonify(films)


# Endpoint to retrieve a list of characters for a given film
@app.route('/films/<int:film_id>/characters', methods=['GET'])
@cache_response_time(seconds=300)
def get_SW_characters(film_id):
    swapi_url = f'https://swapi.dev/api/films/{film_id}/'
    film_data = fetch_SWAPI(swapi_url)
  
    
    if 'characters' in film_data:
        characters = [fetch_SWAPI(character_url) for character_url in film_data['characters']] #fecth different characters from SWAPI
        return jsonify(characters)
    else:
        return jsonify({'error': 'Invalid film ID'}), 404
    

@app.route('/films/<int:film_id>/starships', methods=['GET'])
@cache_response_time(seconds=300)
def get_starships_for_SW(film_id):
    swapi_url = f'https://swapi.dev/api/films/{film_id}/'
    film_data = fetch_SWAPI(swapi_url)
    
    if 'starships' in film_data:
        starships = [fetch_SWAPI(starship_url) for starship_url in film_data['starships']]
        return jsonify(starships)
    else:
        return jsonify({'error': 'Invalid film ID'}), 404
    

# Handling invalid routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Invalid route'}), 404

if __name__ == '__main__':
    app.run(debug=True)
