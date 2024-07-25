from ytmusicapi import YTMusic


class Fetchmoods:
    def __init__(self) -> None:
        self.ytm = YTMusic()
    def getMoodPl(self,params):
        pile_data = []

        for item in self.ytm.get_mood_playlists(params)[:30]:
           
            temp_dict = {'title':item['title'],'playlistid':item['playlistId'],'thumbnail':item['thumbnails'][0]['url']}
            pile_data.append(temp_dict)
        return pile_data