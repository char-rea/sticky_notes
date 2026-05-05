#album management system

class Album:
    def __init__(self, name, songs, artist):
        self.name = name
        self.songs = songs
        self.artist = artist

    def __str__(self):
        return f"{self.name} by {self.artist} with {len(self.songs)} songs"

# list called albums1, add five Album objects to it 
albums1 = [
Album("Shake it offf", ["Shake it off", "Blank Space", "Style"], "Taylor Swift"),
Album("Divide", ["Shape of You", "Castle on the Hill", "Perfect"], "Ed Sheeran"),
Album("1989", ["Blank Space", "Style", "Shake It Off"], "Taylor Swift"),
Album("Purpose", ["Sorry", "Love Yourself", "What Do You Mean?"], "Justin Bieber"),
Album("Reputation", ["Ready for It?", "End Game", "I Did Something Bad"], "Taylor Swift")
]

print("albums1:")
for album in albums1:
    print(album)

#Sort the list according to the number_of_songs and print it out. 
def number_of_songs(album):
    return len(album.songs)

print("Albums sorted by number of songs:")
albums1.sort(key=number_of_songs)
for album in albums1:
    print(album)

#Swap the element at position 1 of albums1 with the element at position 2
def swap_positions(albums, pos1, pos2):
    albums[pos1], albums[pos2] = albums[pos2], albums[pos1]

swap_positions(albums1, 1, 2)

print("\nalbums1 after swap:")
for album in albums1:
    print(album)

#create albums 2 and add different albums to it 

albums2 = [
Album("Thriller", ["Thriller", "Beat It", "Billie Jean"], "Michael Jackson"),
Album("Back in Black", ["Hells Bells", "Shoot to Thrill", "Back in Black"], "AC/DC"),
Album("The Dark Side of the Moon", ["Speak to Me", "Breathe", "On the Run"], "Pink Floyd"),
Album("Rumours", ["Dreams", "Go Your Own Way", "The Chain"], "Fleetwood Mac"),  
Album("Hotel California", ["Hotel California", "New Kid in Town", "Life in the Fast Lane"], "Eagles")
]

print("\nalbums2:")
for album in albums2:
    print(album)

#copy albums1 to albums2 and print it out
albums2 = albums1.copy()
print("\nalbums2 after copying albums1:")
for album in albums2:
    print(album)

#add items to albums 2 and print it out

albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 10))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

print("\nalbums2 after adding new albums:")
for album in albums2:
    print(album)

#sort albums2 alphabetically by name and print it out
albums2.sort(key=lambda album: album.name)
print("\nalbums2 sorted alphabetically by name:")
for album in albums2:
    print(album)