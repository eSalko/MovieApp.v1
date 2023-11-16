import requests

api_key = '46aa50b0'
base_url = 'http://www.omdbapi.com/'


def get_movie_details(title):
    parameters = {'apikey': api_key, 't': title}
    response = requests.get(base_url, params=parameters)
    data = response.json()

    if data['Response'] == 'True':
        # print our the movie details
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Plot: {data['Plot']}")
    else:
        print(f"Error: {data['Error']}")


get_movie_details('Inception')
