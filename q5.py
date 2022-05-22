import requests
apiKey = '324034ab'
dataURL='http://www.omdbapi.com/?apiKey='+apiKey

while True:
    year=''
    movieTitle = input("What movie may I tell you about? ")
    if movieTitle=='quit':
        break

    movieTitle = movieTitle.title()

    params ={'s':movieTitle, 'type':'movie','y':year}
    response =requests.get(dataURL,params=params).json()

    for movie in response['Search']:
        if movie['Title'].title()== movieTitle:
            params ={'i':movie['imdbID'], 'type':'movie'}
            response =requests.get(dataURL,params=params).json()
            message = '{} -- {} -- {} \n{}'.format(response['Title'], response['Year'], response['Rated'], response['Plot'])
            print(message)
            print("\n")
            break