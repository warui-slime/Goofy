from mainapp.utils.homepage.fetch_home import Home_page
from mainapp.utils.explorepage.fetch_explore import Explore_page
from mainapp.utils.searches import suggestions
from mainapp.utils.musicfetch.fetchmusic import Downloadmusic
from mainapp.utils.searches.fetchsearch import FetchSearch
from mainapp.utils.mix.fetchPl import Additionalcontent
from mainapp.utils.mix.fetchalbum import Fetchalbum
from mainapp.utils.mix.fetchartist import Fetchartist
from mainapp.utils.mix.fetchmoods import Fetchmoods
from mainapp.utils.mix.songdetails import FetchMusicDetails
from mainapp.utils.mix.fetchrelated import Relatedcontent
from mainapp.utils.mix.fetchlyrics import Lyrics


import asyncio

class Goofyapi():
    async def get_homepage(self):
        inst = Home_page()
       

        ribbon,heading1, heading2, heading3, heading4, heading5 = await asyncio.gather(
            inst.getRibbonData(),
            inst.get_heading1(),
            inst.get_heading2(),
            inst.get_heading3(),
            inst.get_heading4(),
            inst.get_heading5()
        )
        return {
            'ribbon':ribbon,
            'heading1': heading1,
            'heading2': heading2,
            'heading3': heading3,
            'heading4': heading4,
            'heading5': heading5
        }
    

    async def get_explore(self):
        inst = Explore_page()
        heading1, heading2, heading3, heading4 = await asyncio.gather(inst.get_heading1(), inst.get_heading2(), inst.get_heading3(), inst.get_heading4())

        return {
            'heading1': heading1,
            'heading2': heading2,
            'heading3':heading3,
            'heading4':heading4
        }
    
    def get_explore_sync(self):
        return asyncio.run(self.get_explore())
    
    def get_homepage_sync(self):
        return asyncio.run(self.get_homepage())
    
    def get_suggestions(self,query):
        return asyncio.run(suggestions.main(query))
    
    def getMusic(self,videoIds):
        Downloadmusic.download(videoIds)
        return {}
    
    def getSearch(self,query):
        ins = FetchSearch()
        return {'searchdata':ins.getSongs(query)}
    def getPlaylist(self,query):
        ins = Additionalcontent()
        
        return {'pldata':ins.getPlaylist(query)}
    def getAlbum(self,query):
        ins = Fetchalbum()
        return {'aldata':ins.getAlbum(query)}
    
    def getArtist(self,query):
        ins = Fetchartist()
        return {'ardata':ins.getArtist(query)}
    
    def getMoodpl(self,query):
        ins = Fetchmoods()
        return {'mooddata':ins.getMoodPl(query)}

    def getSongdetails(self,songIds):
        ins = FetchMusicDetails()
        return {'songsdetail':asyncio.run(ins.get_song_details(songIds))}
    
    def getRelated(self,query):
        ins = Relatedcontent()
        return {'related' :ins.getRelated(query)}
    
    def getLyrics(self,query):
        ins = Lyrics()
        return {"lyrics":ins.getLyrics(query)}