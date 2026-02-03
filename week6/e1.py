# Exercise 1: Music Library Manager
from collections import Counter

# 1. Initialize Data Structures
# TODO: Create an empty list or dictionary to store your music library.
#Each music entry could be a dictionary with keys like 'title', 'artist', 'genre', 'duration'.
# Example:
# music_library = []
music_library = [
    {
        "title": "Song 1",
        "artist": "Artist 1",
        "genre": "Rock",
        "duration": 100
    },
    {
        "title": "Song 2",
        "artist": "Artist 2",
        "genre": "Rock",
        "duration": 200
    },
    {
        "title": "Song 3",
        "artist": "Artist 3",
        "genre": "Pop",
        "duration": 300
    },
    {
        "title": "Song 4",
        "artist": "Artist 4",
        "genre": "Blues",
        "duration": 400
    },
]


# 2. Function to Add Music
# TODO: Define a function that takes music details (title, artist, genre, duration)
#and adds it to your music_library.
#Consider adding validation for input.
# def add_song(library, title, artist, genre, duration):
## ... implementation ...
#pass
def add_song(library, title, artist, genre, duration):
    library.append({
        "title": title,
        "artist": artist,
        "genre": genre,
        "duration": duration
    })

# 3. Function to Display Music Library
# TODO: Define a function that prints all songs in the library in a formatted way.
#Include options for filtering by artist or genre.
# def display_library(library, filter_artist=None, filter_genre=None):
## ... implementation ...
#pass
def display_library(library, filter_artist=None, filter_genre=None):
    for song in library:
        if filter_artist and song["artist"] != filter_artist:
            continue
        if filter_genre and song["genre"] != filter_genre:
            continue
        print(f"{song['title']} - {song['artist']} - {song['genre']} - {song['duration']}")

# 4. Main Program Loop
# TODO: Implement a loop that allows the user to:
#- Add new songs
while True:
    print("Menu:")
    print("1. Add a new song")
    print("2. View all songs and Statistics")
    print("3. Filter songs by artist")
    print("4. Filter songs by genre")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        title = input("Enter the title: ")
        artist = input("Enter the artist: ")
        genre = input("Enter the genre: ")
        duration = input("Enter the duration: ")
        add_song(music_library, title, artist, genre, duration)
    elif choice == '2':
        display_library(music_library)
        print("Statistics:")
        print(f"Total songs: {len(music_library)}")
        print(f"Total duration: {sum(song['duration'] for song in music_library)}")
        print("Genre Statistics:")
        genre_counts = Counter(song["genre"] for song in music_library)
        for genre, count in genre_counts.items():
            print(f"{genre}: {count}")

    elif choice == '3':
        filter_artist = input("Enter the artist: ")
        display_library(music_library, filter_artist=filter_artist)
    elif choice == '4':
        filter_genre = input("Enter the genre: ")
        display_library(music_library, filter_genre=filter_genre)
    elif choice == '5':
        break
    else:
        print("Invalid choice")

#- View the entire library
#- View songs by a specific artist or genre
#- Exit the program
#Use clear prompts and messages.
# Example usage (after implementing functions):
# while True:
#print("\nMusic Library Menu:")
#print("1. Add a new song")
#print("2. View all songs")
#print("3. Filter songs by artist")
#print("4. Filter songs by genre")
#print("5. Exit")
#choice = input("Enter your choice: ")
#if choice == '1':
#
#
#
#
#
# ... collect input and call add_song ...
#pass
#elif choice == '5':
#break
# ... other choices ...