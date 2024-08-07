import httpx
import asyncio

class FetchMusicDetails:
    def __init__(self) -> None:
        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    async def fetch_song_detail(self, client, sid):
        url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={sid}"
        response = await client.get(url, headers=self.headers)
        data = response.json()
        return {'title': data['title'], 'author': data["author_name"].replace(" - Topic", ""), "thumbnail": data["thumbnail_url"],"songId":sid}

    async def get_song_details(self, song_ids: list):
        async with httpx.AsyncClient() as client:
            tasks = [self.fetch_song_detail(client, sid) for sid in song_ids]
            results = await asyncio.gather(*tasks)
        return results
