class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday do you",
                   "I don't want to get sued",
                   "So I'll stop right there"]) #happy_bday相当于self  而歌词字符串相当于lyrics

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

#print("happy_bday.lyrics<===>", happy_bday.lyrics)
happy_bday.sing_me_a_song()
#print("\n")

#print("bulls_on_parade.lyrics<===>", bulls_on_parade.lyrics)
bulls_on_parade.sing_me_a_song()
