from ytmusicapi import YTMusic

class Lyrics:
    def __init__(self) -> None:
        self.ytm = YTMusic()
    def getLyrics(self,videoId):
        song_data = self.ytm.get_watch_playlist(videoId)
        pile_data = {"lyrics":"","thumbnail":song_data["tracks"][0]["thumbnail"][-1]["url"]}
        try:
            pile_data["lyrics"] = self.ytm.get_lyrics(song_data["lyrics"])["lyrics"]
        except Exception:
            pass
        return pile_data