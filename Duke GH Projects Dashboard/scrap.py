import re 
import csv
import pandas as pd

data = []


from requests_html import HTMLSession
s = HTMLSession()

data = []

def get_project_details(name, url):

    extract = {}

    extract["project"] = name

    url = url

    #url = 'https://globalhealth.duke.edu/projects/tanzanian-adolescent-hiv-prevention-and-treatment-implementation-science-alliance-t-ahisa'
    
    r = s.get(url)


    a  = r.html.find('div.list__group')

    for i in a:

        x = i.text

        key = re.findall(r".+?(?=:)",x)[0]

        value = re.findall(r"(?<=\n)[^\]]+",x)[0]

        value = value.replace('\n','')

        value = value.strip()

        extract[key] = value


    try:
        b  = r.html.find('div.field--field-description')[0]
        b = b.text
        b = b.replace('\n','')
        extract["desc"] = b.strip()
    except:
        b = ''
        

    data.append(extract)



with open('gh_duke_project_links.csv', newline='') as f:
    reader = csv.reader(f)
    project = list(reader)


#print(type(project))

for i in project:
    #i  = project[i]
    get_project_details(i[0], i[1])


df = pd.DataFrame(data)
df.index = df.index + 1


df.to_csv("final_data.tsv", encoding='utf-8', index=True,sep = "\t",index_label = "id")







