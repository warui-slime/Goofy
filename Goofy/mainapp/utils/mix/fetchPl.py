from ytmusicapi import YTMusic


class Additionalcontent:
    def __init__(self) -> None:
        self.ytm = YTMusic()
    def getPlaylist(self,playlistId):
        pile_data = []

        for item in self.ytm.get_playlist(playlistId)['tracks']:
            if item['thumbnails'][0]['width'] < 400:
                continue
            temp_dict = {'title':item['title'],'author':item['artists'][0]['name'],'videoId':item['videoId'],'thumbnail':item['thumbnails'][0]['url'],'duration':item['duration']}
            pile_data.append(temp_dict)
        return pile_data