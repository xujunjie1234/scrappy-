import scrapy
from wanyiyun.items import WanyiyunItem
import pandas as pd
import json
import datetime

class DoubanSpiderSpider(scrapy.Spider):
    name = 'wanyiyun'
    def __init__(self):
        df = pd.read_csv('C:\\Python\\Python37\\python_pachong\\song.csv')
        data = df.drop_duplicates(['id'])[38191:]
        data = data.reset_index()
        urls = ['http://music.163.com/api/v1/resource/comments/R_SO_4_{}?csrf_token='.format(i) for i in data['id']]
        self.urls = urls
        self.songs = data['song']
        self.i = -1
        self.n = 306457

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        wanyi_item = WanyiyunItem()
        self.i += 1
        js = json.loads(response.text)
        hotcomments = js['hotComments']
        for info in hotcomments:
            nickname = info['user']['nickname']
        # 
            timestamp = info['time']
            utc_time = datetime.datetime.utcfromtimestamp(timestamp//1000)
            date = utc_time + datetime.timedelta(hours=8)
            # 
            content = info['content']
            likecount = info['likedCount']  

            wanyi_item['nickname'] = nickname     
            wanyi_item['date'] = str(date)
            wanyi_item['likecount'] = likecount     
            wanyi_item['content'] = content 
               
            wanyi_item['song'] = self.songs[self.i]  
            wanyi_item['number'] = self.n     

            self.n += 1
            
            yield wanyi_item
        

