from ytmusicapi import YTMusic
import requests

class Fetchalbum:
    def __init__(self):
        self.ytm = YTMusic()
   
    def getAlbum(self,browseId):
        pile_data = []

        for item in self.ytm.get_album(browseId)['tracks']:
            temp_dict = {'title':item['title'],'author':item['artists'][0]['name'],'videoId':item['videoId'],'duration':item['duration']}
            temp_dict['thumbnail'] = requests.get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={item['videoId']}").json()['thumbnail_url']
            pile_data.append(temp_dict)
        return pile_data