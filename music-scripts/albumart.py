from mpd import MPDClient
import subprocess
import time

album_file = "/tmp/album.png"
mpd_host = "nitori"

def dl_album(client, song):
    img = client.albumart(song)['binary']
    f = open(album_file,'wb')
    f.write(img)
    f.close()

if (__name__ == '__main__'):

    client = MPDClient()
    
    client.connect(mpd_host,6600)
    curr_song = client.currentsong()['file']
    dl_album(client, curr_song)
    client.disconnect()
    subprocess.Popen(["feh","/tmp/album.png"])
    
    while (True):
        client.connect(mpd_host,6600)
        new_song = client.currentsong()['file']
        # print(new_song)
        if (new_song != curr_song):
            # print("song changed")
            curr_song = new_song
            dl_album(client, curr_song)
        client.disconnect()
        time.sleep(10)
    