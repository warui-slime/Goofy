import yt_dlp
import os

class Downloadmusic:
    def download(videoIds:list[str])->None:
        try:
            os.remove("mainapp/static/mainapp/player/songs/song.m4a")
        except FileNotFoundError:
            pass    
        ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'quiet': True,
        'outtmpl':"mainapp/static/mainapp/player/songs/%(id)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'parallel': True,
        'concurrent-fragments': 10,
        # 'buffer_size': 1024 * 16,
        'ignoreerrors':True,
        "socket_timeout":6
        }

        if len(videoIds) == 1:
            ydl_opts['ignoreerrors'] = False
            # ydl_opts['outtmpl'] = "mainapp/static/mainapp/player/songs/song.m4a"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(videoIds)