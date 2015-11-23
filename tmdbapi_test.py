import requests


def request_page(namespace, page_number):

    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/'

    request_url = '{0}{1}?api_key={2}&page={3}'.format(
        root_url,
        namespace,
        api_key,
        page_number
    )
    print request_url
    response = requests.get(request_url)
    data = response.json()
    return data


def write_json(movie_list):

    for movie in movie_list:
        movie_id = movie['id']
        filename = 'movies/{0}.json'.format(movie_id)
        f = open(filename, 'w')
        f.write(str(movie))
        f.close()


def parse_response(url, page_number):

    data = request_page(url, page_number)
    total_pages = int(data['total_pages'])
    write_json(data['results'])

    return total_pages


def get_movies():

    movies_urls = [
        'movie/popular',
        'movie/latest',
        'movie/top_rated'
    ]

    for url in movies_urls:
        total_pages = parse_response(url, 1)
        for next_page in range(2, total_pages+1):
            parse_response(url, next_page)


if __name__ == '__main__':
    get_movies()
