import requests

URL_TYPES = ['track', 'artist', 'album', 'playlist']
API_URL = 'https://api.deezer.com/'

TRACK_URL = API_URL + URL_TYPES[0]
ARTIST_URL = API_URL + URL_TYPES[1]
ALBUM_URL = API_URL + URL_TYPES[2]
PLAYLIST_URL = API_URL + URL_TYPES[3]

EXPLICIT_CONTENT = {
    0: 'Not Explicit',
    1: 'Explicit',
    2: 'Unknown',
    3: 'Edited',
    6: 'No Advice Available'
 }

class Deezer:
    '''
    Main Deezer class 🎵
    it contains:
        A method to check if the provided url is a valid deezer url
        A method to search with the official deezer apis
    '''
    
    def is_valid_url(self, url) -> bool:
        '''
        this method returns True if the url is valid
        '''
        if url:
            return url.split('?')[0].split('/')[-2] in URL_TYPES

    def search(self, text: str, method: str) -> 'generator':
        '''
        this method returns an object
        '''
        if method not in URL_TYPES:
            raise self.NotValidMethod()

        base = API_URL + 'search/' + method + '/'
        par = {'q': text}

        classes = Track, Artist, Album, Playlist
        modes = {el: cl for el, cl in zip(URL_TYPES, classes)}
        mode = modes.get(method)

        for elem in requests.get(base, par).json()['data']:
                yield mode(elem['id'])

    class NotValidMethod(Exception):
        def __str__(self):
            return 'method must be in ' + ', '.join(URL_TYPES)

class Artist:
    '''
    This class is used to init Artist objects
    '''
    def __init__(self, id):

        r = requests.get('{}/{}'.format(ARTIST_URL, id)).json()

        self.id = r.get('id')
        self.name = r.get('name')
        self.link = r.get('link')
        self.share = r.get('share')
        self.picture = r.get('picture')
        self.picture_small = r.get('picture_small')
        self.picture_medium = r.get('picture_medium')
        self.picture_big = r.get('picture_big')
        self.picture_xl = r.get('picture_xl')
        self.nb_album = r.get('nb_album')
        self.nb_fan = r.get('nb_fan')
        self.radio = r.get('radio')
        self.tracklist = r.get('tracklist')
        self.albums = self.get_albums(requests.get(
            '{}/{}/{}'.format(ARTIST_URL, id, 'albums')).json()['data'])

    def get_albums(self, albums_data: list) -> 'generator':
        for album in albums_data:
            yield Album(album['id'])


class Album:
    '''
    This class is used to init Album objects
    '''
    def __init__(self, id):

        r = requests.get('{}/{}'.format(ALBUM_URL, id)).json()

        self.id = r.get('id')
        self.title = r.get('title')
        self.upc = r.get('upc')
        self.link = r.get('link')
        self.share = r.get('share')
        self.cover = r.get('cover')
        self.cover_small = r.get('cover_small')
        self.cover_medium = r.get('cover_medium')
        self.cover_big = r.get('cover_big')
        self.cover_xl = r.get('cover_xl')
        self.genre_id = r.get('genre_id')
        self.genres = r.get('genres')
        self.label = r.get('label')
        self.nb_tracks = r.get('nb_tracks')
        self.duration = r.get('duration')
        self.fans = r.get('fans')
        self.rating = r.get('rating')
        self.release_date = r.get('release_date')
        self.record_type = r.get('record_type')
        self.available = r.get('available')
        self.tracklist = r.get('tracklist')
        self.explicit_lyrics = r.get('explicit_lyrics')
        self.explicit_content_lyrics = EXPLICIT_CONTENT.get(r.get('explicit_content_lyrics'))
        self.explicit_content_cover = EXPLICIT_CONTENT.get(r.get('explicit_content_cover'))
        self.contributors = r.get('contributors')
        self.artist = Artist(r.get('artist').get('id'))
        self.tracks = self.get_tracks(requests.get(
            '{}/{}/{}'.format(ALBUM_URL, id, 'tracks')).json()['data'])

    def get_tracks(self, tracks_data: list) -> 'generator':
        '''
        this method returns a generator object containing
        all the track object of a given tracks data
        '''
        for track in tracks_data:
            yield Track(track['id'])

class Track:
    '''
    This class is used to init Track objects
    '''
    def __init__(self, id):

        r = requests.get('{}/{}'.format(TRACK_URL, id)).json()

        self.id = r.get('id')
        self.readable = r.get('readable')
        self.title = r.get('title')
        self.title_short = r.get('title_short')
        self.title_version = r.get('title_version')
        self.unseen = r.get('unseen')
        self.isrc = r.get('isrc')
        self.link = r.get('link')
        self.share = r.get('share')
        self.duration = r.get('duration')
        self.track_position = r.get('track_position')
        self.disk_number = r.get('disk_number')
        self.rank = r.get('rank')
        self.release_date = r.get('release_date')
        self.explicit_lyrics = r.get('explicit_lyrics')
        self.explicit_content_lyrics = EXPLICIT_CONTENT.get(r.get('explicit_content_lyrics'))
        self.explicit_content_cover = EXPLICIT_CONTENT.get(r.get('explicit_content_cover'))
        self.preview = r.get('preview')
        self.bpm = r.get('bpm')
        self.gain = r.get('gain')
        self.available_countries = r.get('available_countrie')
        self.artist = Artist(r.get('artist').get('id'))
        self.album = Album(r.get('album').get('id'))


class Playlist:
    '''
    This class is used to init Playlist objects
    '''
    def __init__(self, id):

        r = requests.get('{}/{}'.format(PLAYLIST_URL, id)).json()

        self.id = r.get('id')
        self.title = r.get('title')
        self.description = r.get('description')
        self.duration = r.get('duration')
        self.public = r.get('public')
        self.is_loved_track = r.get('is_loved_track')
        self.collaborative = r.get('collaborative')
        self.rating = r.get('rating')
        self.nb_tracks = r.get('nb_tracks')
        self.unseen_track_count = r.get('unseen_track_count')
        self.fans = r.get('fans')
        self.link = r.get('link')
        self.share = r.get('share')
        self.picture = r.get('picture')
        self.picture_medium = r.get('picture_medium')
        self.picture_big = r.get('picture_big')
        self.picture_xl = r.get('picture_xl')
        self.creator = r.get('creator')

        self.tracks = self.get_tracks(requests.get(
            '{}/{}/{}'.format(PLAYLIST_URL, id, 'tracks')).json()['data'])

    def get_tracks(self, tracks_data: list) -> 'generator':
        '''
        this method returns a generator object containing
        all the track object of a given tracks data
        '''
        for track in tracks_data:
            yield Track(track['id'])
