# import the main class
from deezer import Deezer


def main():

    print('\nThis script will print out every album and song of a specific artist.')

    # initialize the main class
    deezer = Deezer()

    # taking the user input
    user_input = input('What artist do you want to see? > ').lower()

    # creating a generator object with all the artists found
    artists = deezer.search(user_input, 'artist')

    album_count = 1
    track_count = 1

    for artist in artists:

        # if the specific artis is found
        if artist.name.lower() == user_input:

            # print artist name
            print('\nArtist: %s\n' % (artist.name))

            # for every album of the artist
            for album in artist.albums():
                
                # print current count and album name
                print('Album: %s - %s\n' % (album_count, album.title))

                # every new album increment this counter
                album_count += 1

                # for every track of every album
                for track in album.tracks():

                    # print current track count and track title
                    print('\tTrack: %s - %s' % (track_count, track.title))

                    # every new track increment this counter
                    track_count +=1

                # reset the track count every new album and print new line
                track_count = 1
                print()

# start the script
if __name__ == "__main__":
    main()