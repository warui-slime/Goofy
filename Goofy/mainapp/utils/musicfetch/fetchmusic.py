import yt_dlp
import os

class Downloadmusic:
    def download(videoId:str)->None:
        try:
            os.remove("mainapp/static/mainapp/player/song.m4a")
        except FileNotFoundError:
            pass    
        ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'quiet':'true',
        'outtmpl':"mainapp/static/mainapp/player/song.m4a",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'parallel': True,
        'concurrent-fragments': 10,
        # 'buffer_size': 1024 * 16,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([videoId])