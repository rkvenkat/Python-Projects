import scrapy
import re

url = 'https://www.americangaming.org/research/state-gaming-map'

state_list_html = response.css('select[name="state"]')
states_list = state_list_html.css('option').getall()

state = []

for i in states_list:
    a = re.findall(r'(?<=value=")(.*)(?=" )',i)
    if len(a) != 0:
        state.append(a[0])










