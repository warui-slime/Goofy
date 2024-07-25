import warnings
import httpx
import re
import json
import asyncio


warnings.filterwarnings("ignore", category=DeprecationWarning)


class Songsearch:
    def __init__(self,songname:str) -> None:
        self.songname = songname
        self.suggestiondict = {"songs":[],"artists":[],"card":{}}
        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    async def get_info(self,videoId:str,is_card:bool=False,song_artist:bool = False)->None:
        info_dict:dict = httpx.get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={videoId}",headers=self.headers).json()
        info_dict.pop("provider_url")
        info_dict.pop("type")
        info_dict.pop("thumbnail_height")
        info_dict.pop("thumbnail_width")
        info_dict.pop("width")
        info_dict.pop("height")
        info_dict.pop("html")
        info_dict.pop("provider_name")
        info_dict.pop("version")
        info_dict["author_name"] = info_dict["author_name"].replace(" - Topic","")
        info_dict['videoId'] = videoId
        
        if is_card and info_dict['author_name'] != "Various Artists":
            self.suggestiondict["card"] = info_dict
            self.suggestiondict["artists"].append({"author_name":info_dict["author_name"],"thumbnail_url":eval(re.findall(r'"avatar":\{"thumbnails":\[([\s\S]*?)\]\}',httpx.get(info_dict["author_url"],headers=self.headers).content.decode("unicode_escape"))[-1])["url"],'author_id':info_dict['author_url'].replace('https://www.youtube.com/channel/',"")})
        else:
            # print(re.findall(r'"avatar":\{"thumbnails":\[([\s\S]*?)\]\}',httpx.get(info_dict["author_url"],headers=self.headers).content.decode("unicode_escape"))[-1])
            self.suggestiondict["songs"].append(info_dict)
            if song_artist and info_dict['author_name'] != "Various Artists":
                self.suggestiondict["artists"].append({"author_name":info_dict["author_name"],"thumbnail_url":eval(re.findall(r'"avatar":\{"thumbnails":\[([\s\S]*?)\]\}',httpx.get(info_dict["author_url"],headers=self.headers).content.decode("unicode_escape"))[-1])["url"],'author_id':info_dict['author_url'].replace('https://www.youtube.com/channel/',"")})

    async def songsearch(self)->dict:
        page = httpx.get(f"https://music.youtube.com/search?q={self.songname}", headers=self.headers).content.decode("unicode_escape")
        m:list = json.loads(re.findall(r'JSON.parse\(\'\{"query":"(.*)"\}\'\), data: ([\s\S]*?)}\);ytcfg.set',page)[0][1][1:-1])["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"]
        card = None
        for i in m:
            if "musicCardShelfRenderer" in i.keys():
                if i["musicCardShelfRenderer"]["subtitle"]["runs"][0]["text"] in ("Video","Song"):
                    try:
                        card=i["musicCardShelfRenderer"]["contents"][1]["musicResponsiveListItemRenderer"]["flexColumns"][0]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["navigationEndpoint"]["watchEndpoint"]["videoId"]
                    except KeyError:
                        pass    
            elif "musicShelfRenderer" in i.keys():
                if i["musicShelfRenderer"]["title"]["runs"][0]["text"] == "Songs":
                    song1=i["musicShelfRenderer"]["contents"][0]["musicResponsiveListItemRenderer"]["flexColumns"][0]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["navigationEndpoint"]["watchEndpoint"]["videoId"]

                    song2=i["musicShelfRenderer"]["contents"][1]["musicResponsiveListItemRenderer"]["flexColumns"][0]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["navigationEndpoint"]["watchEndpoint"]["videoId"]
                    
                    song3=i["musicShelfRenderer"]["contents"][2]["musicResponsiveListItemRenderer"]["flexColumns"][0]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["navigationEndpoint"]["watchEndpoint"]["videoId"]
                    
                    
                    if card is not None:
                        await asyncio.gather(self.get_info(song1,song_artist=True),self.get_info(song2),self.get_info(song3),self.get_info(card,is_card=True))
                    else:
                        await asyncio.gather(self.get_info(song1,song_artist=True),self.get_info(song2,song_artist=True),self.get_info(song3))
                    return self.suggestiondict
    

async def main(query):
 
    inst = Songsearch(query)
    try:
        return await inst.songsearch()
    except (asyncio.CancelledError,IndexError):
        pass
    
# def search(query):
#     return asyncio.run(main(query))
    

