from ytmusicapi import YTMusic


class Relatedcontent:
    def __init__(self) -> None:
        self.ytm = YTMusic()
    def getRelated(self,videoId):
        pile_data = []

        for item in self.ytm.get_watch_playlist(videoId=videoId)['tracks'][1:]:

            temp_dict = {'title':item['title'],'author':item['artists'][0]['name'],'videoId':item['videoId'],'thumbnail':item['thumbnail'][1]['url']}
            pile_data.append(temp_dict)
        return pile_data 