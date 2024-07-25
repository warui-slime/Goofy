from ytmusicapi import YTMusic
import random



class Explore_page:
    def __init__(self) -> None:
        self.ytm = YTMusic()

   

    async def get_heading1(self):
        nsongs = self.ytm.search('latest songs',filter='songs',limit=10)
        pile_data = []
        for item in nsongs:
            if item['artists']:
                item['artists'][0]['name'] = item['artists'][0]['name'] 
                item['title'] = item['title']
                temp_dict = {
                 'title': item['title'],
                 'artist': item['artists'][0]['name'],
                 'thumbnail': item['thumbnails'][1]['url'],
                 'videoId' : item['videoId']
                }
                pile_data.append(temp_dict)
        return pile_data


    async def get_heading2(self):
        cplaylists = self.ytm.search('top playlists',filter='community_playlists',limit=10)
        # cplaylists = self.ytm.search('top playlists',filter='featured_playlists',limit=10)
        pile_data = []
        for item in cplaylists:
            
            for pic in item['thumbnails']:
                if pic['width'] > 120:
                    temp_dict = {
                    'title': item['title'],
                    'thumbnail': pic['url'],
                    'browseId' : item['browseId']
                    }
                    pile_data.append(temp_dict)
                    break
        return pile_data


    async def get_heading3(self):
        mood_colors = [ "bg-gradient-to-r from-[#7a2828] via-[#d29393] to-[#7a2828]", "bg-gradient-to-r from-[#FF75C5] via-[#FFB6E0] to-[#FF75C5]", "bg-gradient-to-r from-[#467b3d] via-[#b0f1a5] to-[#467b3d]", "bg-gradient-to-r from-[#66DDEE] via-[#B3F5FF] to-[#66DDEE]"]

       
        moods = self.ytm.get_mood_categories()
        pile_data = []
        pile_data.extend(moods['Moods & moments'])
        pile_data.extend(random.sample(moods['Genres'],26))
        for i in range(36):
            pile_data[i]['mcolor'] = mood_colors[random.randint(0,3)]
        return pile_data
    
    async def get_heading4(self):
        talb = self.ytm.search('trending albums',filter='albums')
        pile_data =[]
        pile_data = []
        for item in talb:
            item['artists'][0]['name'] = item['artists'][0]['name'] 
                
            item['title'] = item['title']       
            temp_dict = {
                 'title': item['title'],
                 'artist': item['artists'][0]['name'],
                 'thumbnail': item['thumbnails'][-2]['url'],
                 'browseId' : item['browseId']
            }
            pile_data.append(temp_dict)
        return pile_data


    