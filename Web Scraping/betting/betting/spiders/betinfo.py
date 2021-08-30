import scrapy
import re

from betting.items import BettingItem

info = []

class BetinfoSpider(scrapy.Spider):
    name = 'betinfo'

    start_urls = ['https://www.americangaming.org/research/state-gaming-map']
    

    def parse(self, response):
        state_list_html = response.css('select[name="state"]')
        states_list = state_list_html.css('option').getall()

        state = []
        

        for i in states_list:
            a = re.findall(r'(?<=value=")(.*)(?=" )',i)
            b = re.findall(r'(?<=>)(.*)(?=<)',i)
            if len(a) != 0:
                state.append([a[0],b[0]])

        for i in state:
            next_link = f'https://www.americangaming.org/state/{i[0]}/?type=activity'  
            yield scrapy.Request(url = next_link
                                ,meta = {'state':i[0]}
                                ,callback = self.newfunction)    
        


    def newfunction(self, response):
        a = response.css('p[class="states-activity"]::text').get()
        b = response.meta['state']
        yield BettingItem( state = b,status = a)
       

            
        