# song.py

class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update the total count of songs
        Song.count += 1
        
        # Update genre tracking
        if genre not in Song.genres:
            Song.genres.add(genre)
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update artist tracking
        if artist not in Song.artists:
            Song.artists.add(artist)
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
