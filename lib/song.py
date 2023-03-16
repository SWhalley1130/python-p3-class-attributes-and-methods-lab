class Song:

    count = 0
    artists=[]
    genres=[]
    genre_count={}
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.add_song_to_count()
        self.add_to_genres(self)
        self.add_to_artists(self)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count=cls.count+1

    @classmethod
    def add_to_genres(cls,self):   
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)

    @classmethod
    def add_to_artists(cls,self): 
        if self.artist not in cls.artists:
           cls.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls, self):
        if cls.genre_count.get(self.genre)==None:
            cls.genre_count[self.genre]=1
        else:
            cls.genre_count[self.genre]+=1

    @classmethod
    def add_to_artist_count(cls, self):
        if cls.artist_count.get(self.artist)==None:
            cls.artist_count[self.artist]=1
        else:
            cls.artist_count[self.artist]+=1

    






    
