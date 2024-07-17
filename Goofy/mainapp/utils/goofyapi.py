from mainapp.utils.homepage.fetch_home import Home_page
from mainapp.utils.explorepage.fetch_explore import Explore_page
import asyncio

class Goofyapi():
    async def get_homepage(self):
        inst = Home_page()
       

        heading1, heading2, heading3, heading4, heading5 = await asyncio.gather(
            inst.get_heading1(),
            inst.get_heading2(),
            inst.get_heading3(),
            inst.get_heading4(),
            inst.get_heading5()
        )
        return {
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
    
