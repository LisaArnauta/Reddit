import asyncio
import aiohttp
import json

async def request_data(url):
    async with aiohttp.request('GET',url) as gt_dt:
        return gt_dt.read()
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str

async def get_reddit_top(subreddit):
    data = await request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5')
    # use request_data coroutine to get reddit top
    # url pattern - f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'

    # then unpack data to json:
    
    j = json.loads(data)
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        
# % reddit_name %: {
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     },
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     }
    # }
    
reddit_top = {title :{'score': int(score),'link':str(link)}}
        top = {subreddit : reddit_top}

        return  top
    
async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"}
    
# use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
 # try to use *args instead of hardcoded function calls        
    res = await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))
    print(res)

asyncio.run(main())
