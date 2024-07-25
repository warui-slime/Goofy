from ytmusicapi import YTMusic


class Fetchartist:
    def __init__(self) -> None:
        self.ytm = YTMusic()
    def getArtist(self,browseId):
        pile_data = {'singles':[],'songs':[],'albums':[]}
        artist_data = self.ytm.get_artist(browseId)

        for single in artist_data["singles"]['results']:
            pile_data['singles'].append({'title':single['title'],'browseId':single['browseId'],'thumbnail':single['thumbnails'][0]['url']})

        for song in artist_data["songs"]['results']:
            pile_data['songs'].append({'title':song['title'],'videoId':song['videoId'],'thumbnail': song['thumbnails'][1]['url']})

        for album in artist_data['albums']['results']:
            pile_data['albums'].append({'title':album['title'],'browseId':album['browseId'],'thumbnail':album['thumbnails'][0]['url']})

        return pile_data
