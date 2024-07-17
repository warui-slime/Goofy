from ytmusicapi import YTMusic
import random



class Explore_page:
    def __init__(self) -> None:
        self.ytm = YTMusic()

    def manage_names(self,name:str,length:int=20) ->str:
        if len(name) > length :
            return name[:length-5] + "..."
        else : return name

    async def get_heading1(self):
        nsongs = self.ytm.search('latest songs',filter='songs',limit=10)
        pile_data = []
        for item in nsongs:
            if item['artists']:
                item['artists'][0]['name'] = self.manage_names(item['artists'][0]['name']) 
                item['title'] = self.manage_names(item['title'])  
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
                    'title': self.manage_names(item['title'],40),
                    'thumbnail': pic['url'],
                    'browseId' : item['browseId']
                    }
                    pile_data.append(temp_dict)
                    break
        return pile_data


    async def get_heading3(self):
        mood_colors = ["#8FFF7D","#FFC061","#FF5A5A","#A57BFF","#76DEFF","#FF75C5","#FF75C5","#8FFF7D","#FFC061","#FF5A5A","#A57BFF","#76DEFF","#76DEFF","#FF75C5","#8FFF7D","#FFC061","#FF5A5A","#A57BFF","#A57BFF","#76DEFF","#FF75C5","#8FFF7D","#FFC061","#FF5A5A","#FF5A5A","#A57BFF","#76DEFF","#FF75C5","#8FFF7D","#FFC061","#FFC061","#FF5A5A","#A57BFF","#76DEFF","#FF75C5","#8FFF7D"]
        random.shuffle(mood_colors)
        moods = self.ytm.get_mood_categories()
        pile_data = []
        pile_data.extend(moods['Moods & moments'])
        pile_data.extend(random.sample(moods['Genres'],26))
        for i in range(36):
            pile_data[i]['mcolor'] = mood_colors[i]
        return pile_data
    
    async def get_heading4(self):
        talb = self.ytm.search('trending albums',filter='albums')
        pile_data =[]
        pile_data = []
        for item in talb:
            item['artists'][0]['name'] = self.manage_names(item['artists'][0]['name']) 
                
            item['title'] = self.manage_names(item['title'])       
            temp_dict = {
                 'title': item['title'],
                 'artist': item['artists'][0]['name'],
                 'thumbnail': item['thumbnails'][-2]['url'],
                 'browseId' : item['browseId']
            }
            pile_data.append(temp_dict)
        return pile_data


    