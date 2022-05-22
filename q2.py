import requests
apiKey = '324034ab'
dataURL='http://www.omdbapi.com/?apiKey='+apiKey

year=''
movieTitle ='Python'
params ={'s':movieTitle, 'type':'movie','y':year}
response =requests.get(dataURL,params=params).json()

for movie in response['Search']:
    if movie['Title']=='Python':
        params ={'i':movie['imdbID'], 'type':'movie'}
        response =requests.get(dataURL,params=params).json()
        message = '{} -- Released on:{} -- Movie length:{}\nwritten by:{}'.format(response['Title'], response['Released'], response['Runtime'], response['Writer'])
        print(message)