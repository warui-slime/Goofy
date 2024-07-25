from ytmusicapi import YTMusic

class FetchSearch:
    def __init__(self) -> None:
        self.ytm = YTMusic()

    def getSongs(self,query):
        songs = self.ytm.search(query,filter="songs",limit=20)
        pile_data = []
        for item in songs:
            temp_dict = {'title':item['title'],'videoId':item['videoId'],'thumbnail':item['thumbnails'][0]['url']}
            try:
                temp_dict['author'] = item['artists'][0]['name']
                temp_dict['duration'] =item['duration']
            except Exception:
                pass
            pile_data.append(temp_dict)
        return pile_data