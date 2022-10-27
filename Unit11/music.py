'''
Author: Andrew Apollo

This Program will
    - 
'''

class Time:
    '''
    This class will
        - initialize Time
    '''
    __slots__ = ["hours" , "minutes", "seconds"]

    def __init__(self, hours , minutes, seconds):
        '''
        This function will
            - initialize Time
        
        Paramaters
            - hours: hours long
            - minutes: minutes long
            - seconds: seconds long
        '''
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    '''
    This class will
        - initalizea a song 
    '''
    __slots__ = ["title", "artist", "duration"]

    def __init__(self, title , artist, duration):
        '''
        This function will
            - initalizea a song

        Paramaters 
            - title: title of song 
            - artist: artist of song
            -duration: how long the song is 
        '''
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    '''
    This Class will
        - initalize an ablum
    '''

    __slots__ = ["title", "artist", "tracks", "total_time"]

    def __init__(self, title, artist):
        '''
        This Function will
            - initalize an ablum
        '''
        self.title = title
        self.artist = artist
        self.tracks = []
        self.total_time = Time(0,0,0)

MELIORA = Album("Meliora", "Ghost")

def get_time(Time):
    '''
    This function will
        - return the time in 0:00:00 format

    Paramaters
        - Time: passsed in Time class
    '''
    return '{}:{:02}:{:02}'.format(Time.hours, Time.minutes, Time.seconds) 

def add_song(Album , song):
    '''
    This function will
        - add the song to the album
        - add the total time of the album
        - convert the seconds into minutes if over 60
        - convert the minutes to hours if over 60
    
    Paramaters
        - Album: Album being passed in
        - song: song being added  
    '''
    
    Album.tracks.append(song)
    Album.total_time.hours += song.duration.hours
    Album.total_time.minutes += song.duration.minutes
    Album.total_time.seconds += song.duration.seconds

    sec_to_min = Album.total_time.seconds // 60
    if sec_to_min >= 1:
        Album.total_time.minutes += sec_to_min
        Album.total_time.seconds += -60 * sec_to_min

    min_to_hours = Album.total_time.minutes // 60
    if min_to_hours >= 1:
        Album.total_time.hours += min_to_hours
        Album.total_time.minutes += -60 * min_to_hours 

def print_album(song_Album):
    '''
    This function will
        - print the album title and artist
        - print each song name, artist and duration
        - print the album length 
    
    Paramaters
        - song_Album: album being passed in
    '''

    print("Album Title:", Album.title)
    print("Album Artist", Album.artist)
    for song in song_Album.tracks:
        print(song.title, song.artist, get_time(song.duration))

    print("Album Length", get_time(song_Album.total_time))

def main():
    
    #Get time test 
    #print(get_time(Time(2,10,2)))

    #Adding the greatest album of all time
    spirit = Song("Spirit", "Ghost", Time(0,5,15))
    pit = Song("From The Pinnicle To The Pit", "Ghost", Time(0,4,3))
    cirice = Song("Cirice", "Ghost", Time(0,6,2))
    spoksonat = Song("Spoksonat", "Ghost", Time(0,0,56))
    he_is = Song("He Is", "Ghost", Time(0,4,13))
    mummy_dust = Song("Mummy Dust", "Ghost", Time(0,4,7))
    majesty = Song("Majesty", "Ghost", Time(0,5,24))
    devil_church = Song("Devil Church", "Ghost", Time(0,1,6))
    absolution = Song("Absolution", "Ghost", Time(0,4,51))
    deus = Song("Deus in Absentia", "Ghost", Time(0,5,38))

    #Part 3 Tests 
    add_song(MELIORA, spirit)
    add_song(MELIORA, pit)
    add_song(MELIORA, cirice)
    add_song(MELIORA, spoksonat)
    add_song(MELIORA, he_is)
    add_song(MELIORA, mummy_dust)
    add_song(MELIORA, majesty)
    add_song(MELIORA, devil_church)
    add_song(MELIORA, absolution)
    add_song(MELIORA, deus)

    print_album(MELIORA)

main()