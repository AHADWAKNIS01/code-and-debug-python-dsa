class playlists:
    def __init__(self):
        self.song=[]

    def __add__(self, song):
        self.songs.append(song)


    def __len__(self):
        return len(self.song)


p=playlists()
p.add("song a")
p.add("song b")
p.add("song c")


print(len(p))