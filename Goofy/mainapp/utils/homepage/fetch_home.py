from ytmusicapi import YTMusic
import random
import asyncio
import aiohttp


class Home_page:
    def __init__(self) -> None:
        self.ytm = YTMusic()
        self.INchart = self.ytm.get_charts('IN')

    

    async def fetch_thumbnail(self, session, item):
        url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={item['videoId']}"
        async with session.get(url) as response:
            thumbnail_url = (await response.json())['thumbnail_url']
            temp_data = {
                'title': item['title'],
                'artist': item['artists'][0]['name'],
                'thumbnail': thumbnail_url,
                'videoId': item['videoId']
            }
            return temp_data

    async def get_heading1(self): 
        home_data = self.ytm.get_home(limit=13)
       
    
        pile_data = []
        for i in home_data:
            
            if "video" in i['title'].lower() or "playlist" in i['title'].lower() or "albums" in i['title'].lower() or "mix" in i['title'].lower():
                continue
           
            
            
            for con in i['contents'][:5]:
                temp_dict = {'title':'','artist':'','thumbnail':'',"Id":[]}

                for pic in con['thumbnails']:
                    if pic['width'] > 120 and pic['height']>=226 :
                        try:
                            temp_dict['artist']=con['artists'][0]['name'] 
                        except Exception:
                            pass
                        temp_dict['title'] = con['title']
                        temp_dict['thumbnail'] = pic['url']
                        for key in con.keys():
                            if key in ['browseId','videoId','playlistId']:
                                temp_dict["Id"].append(key)
                                temp_dict["Id"].append(con[key])

                        pile_data.append(temp_dict)
                        break

        
        random.shuffle(pile_data)
        return pile_data
    


    async def get_heading2(self):
        INchart = self.INchart
        async with aiohttp.ClientSession() as session:
            tasks = []
            for item in INchart['trending']['items']:
                if item['videoId']: 
                    tasks.append(self.fetch_thumbnail(session, item))

            pile_data = await asyncio.gather(*tasks)
        return pile_data   


    async def get_heading3(self):
        alb = self.ytm.search("latest albums",filter='albums',limit=10)
        pile_data = []
        for item in alb:
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
    
    async def get_heading4(self):
        tsongs = self.ytm.search("top songs",filter='songs',limit=20)
        pile_data = []
        for item in tsongs:
            if item['artists']:
                item['artists'][0]['name'] = item['artists'][0]['name']
                item['title'] = item['title']  
                temp_dict = {
                 'title': item['title'],
                 'artist': item['artists'][0]['name'],
                 'thumbnail': item['thumbnails'][0]['url'],
                 'videoId' : item['videoId']
                }
                pile_data.append(temp_dict)
        return pile_data

    async def get_heading5(self):
        trending_artists = self.INchart['artists']
        pile_data = []
        for item in trending_artists['items']:
            temp_dict = {
                 'title': item['title'],
                 'subscribers': item['subscribers'],
                 'thumbnail': item['thumbnails'][1]['url'],
                 'browseId' : item['browseId']
                }
            pile_data.append(temp_dict)
        return pile_data

