import requests
import re
import csv
import pandas as pd

dataset = []



def get_data(link):

    #url = "https://www.federalregister.gov/api/v1/documents/2022-21851?publication_date=2022-10-07"

    r = requests.get(url = link)

    data = r.json()

    abstract = data['abstract']

    try:
        company = re.findall('(?<=manufactured by )(.*)(?=, meets)',abstract)[0]
    except:
        company = ""

    company = company.title().strip()


    try:
        drug = re.findall('(?<=FDA has determined that )(.*)(?=, manufactured)',abstract)[0]
    except:
        drug = ""

    drug = drug.title().strip()

    pub_date = data['publication_date']

    title = data['title']

    dataset.append({"title": title, "pub_date": pub_date, "company": company, "drug": drug, "link":link})


with open('final_data.csv', newline='') as f:
    reader = csv.reader(f)
    links = list(reader)


for i in links:
    get_data(i[:][1])


df = pd.DataFrame(dataset)

df.to_csv("dataset.csv", encoding='utf-8', index=False)
  