class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self,genre):
        if genre not in Song.genres:
            Song.genres.append(genre)

    def add_to_artists(self,artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1