# python-deezer-api
#### Deezer api implemented with python

## 1. Download
```sh
$ git clone https://github.com/NicKoehler/python-deezer-api
```
## 2. Import in your project
put deezer.py in you project's root path and than you can import it

```python
from deezer import Deezer
```

## 3. Time to write some code
Example code:
```python
# initialize the main class
deezer = Deezer()

# creating a generator object with all the artists found
artists = deezer.search('acdc', 'artist')

# print artist.id and artist.name for every artist found
for artist in artists:
    print('Artist ID: %s' % artist.id)
    print('Artist Name: %s' % artist.name)
```

Output:

```sh
Artist ID: 115
Artist Name: AC/DC
```
