import re 
import csv
import pandas as pd

data = []


from requests_html import HTMLSession
s = HTMLSession()


for n in range(0,50):
    url = f'https://www.federalregister.gov/documents/search?conditions%5Bterm%5D=+Issuance+of+Priority+Review+Voucher&page={n+1}'
    r = s.get(url)

    notice = r.html.find('ul.search-result-documents.official.row')[0]


    notice = notice.xpath('//li[contains(@class, "doc-published")]')


    for i in notice:
        x = i
        x = x.find('h5 a')[0]
        title = x.text
        if "Issuance of Priority Review" in title:
            link, = x.links
            r = s.get(link)
            api_link, = r.html.xpath('//a[contains(@href, "api/v1")]')[0].links
            data.append({"link":link,"api_link":api_link})


df = pd.DataFrame(data)

df.to_csv("final_data.csv", encoding='utf-8', index=False ,header = False)




   