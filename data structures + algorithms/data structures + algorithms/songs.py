class Song():
    def __init__(self,title,artist,lyricist,album):
        self.title = title
        self.artist = artist
        self.lyricist = lyricist
        self.album = album

    def get_title(self):
        return self.title
    def set_title(self,title):
        self.title = title

    def get_artist(self):
            return self.artist
    def set_artist(self,artist):
        self.artist = artist

    def get_lyricist(self):
            return self.lyricist
    def set_lyricist(self,lyricist):
        self.lyricist = lyricist

    def get_album(self):
            return self.album
    def set_album(self,album):
        self.album = album

    def play(self):
         print(f"{self.title} is playing")

class Playlist():
    def __init__(self,title,date,owner):
        self.songs = []
        self.num = 0
        self.title = title
        self.date = date
        self.owner = owner

    def get_title(self):
                return self.title
    def set_title(self,title):
        self.title = title

    def get_date(self):
                return self.date
    def set_date(self,date):
        self.date = date

    def get_owner(self):
                return self.owner
    def set_owner(self,owner):
        self.owner = owner

    def add(self,title,artist,lyricist,album):
          song1 = Song(title,artist,lyricist,album)
          self.songs.append(song1)
          print(f"{title} has been added to the {self.title} playlist")

    def remove(self,title):
          for i in self.songs:
                if i.title == title:
                      self.songs.remove(i)
                      print(f"{title} has been removed")
                      break
          else:
                print(f"{title} does not exist in this playlist")

    def playall(self):
          for x in self.songs:
                x.play()

playlist1 = Playlist("playlist1","29.06.26","owner1")
playlist1.add("song1","artist1","lyricist1","album1")
playlist1.add("song2","artist2","lyricist2","album2")
playlist1.playall()
playlist1.remove("song2")
playlist1.playall()
playlist1.remove("song21")