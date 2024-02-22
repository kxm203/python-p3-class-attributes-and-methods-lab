class Song:
    count = 0
    genres = []
    artists = []
    songs_per_artist = {}
    songs_per_genre = {}
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increment_song_count()
        self.update_genres_and_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
       

    @staticmethod
    def increment_song_count():
        Song.count += 1

    def update_genres_and_artists(self):
        if not hasattr(self, 'genres'):
            self.genres = [] 
        if self.genre not in self.genres:
            self.genres.append(self.genre)

        if not hasattr(self, 'artists'):
            self.artists = [] 
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] +=1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] +=1
        else:
            Song.artist_count[self.artist] = 1



