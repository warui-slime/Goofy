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
        mood_colors = [ "border-l-[#8FFF7D] text-[#8FFF7D] hover:shadow-[#8FFF7D] border-[#8FFF7D]", "border-l-[#FFC061] text-[#FFC061] hover:shadow-[#FFC061] border-[#FFC061]", "border-l-[#FF5A5A] text-[#FF5A5A] hover:shadow-[#FF5A5A] border-[#FF5A5A]", "border-l-[#A57BFF] text-[#A57BFF] hover:shadow-[#A57BFF] border-[#A57BFF]","border-l-[#76DEFF] text-[#76DEFF] hover:shadow-[#76DEFF] border-[#76DEFF]","border-l-[#FF75C5] text-[#FF75C5] hover:shadow-[#FF75C5] border-[#FF75C5]"]

       
        moods = self.ytm.get_mood_categories()
        pile_data = []
        pile_data.extend(moods['Moods & moments'])
        pile_data.extend(random.sample(moods['Genres'],26))
        num_colors = len(mood_colors)
        num_columns = 6  # Adjust this based on your actual layout

        for i in range(len(pile_data)):
            # Calculate the diagonal index for the current item
            diagonal_index = (i // num_columns - i % num_columns) % num_colors
            pile_data[i]['mcolor'] = mood_colors[diagonal_index]
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


    