import requests

data = requests.get('https://twitchemotes.com/api_cache/v2/images.json').json()
EMOTE_URL = 'https://static-cdn.jtvnw.net/emoticons/v1/{id}/1.0'
emotes = data['images']

with open('emotelist.txt', 'w') as myFile:
    for id, obj in emotes.iteritems():
        myFile.write('{} {}\n'.format(obj['code'], EMOTE_URL.format(id=id)))

