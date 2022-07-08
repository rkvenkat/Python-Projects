import pandas as pd
import re 
import csv

student_details = []


def get_details(url):
    
    from requests_html import HTMLSession
    s = HTMLSession()
    url = url
    r = s.get(url)
    details = r.html.find('div.dmach-acf-item-content')
    extract = details[0].text

    try:
        country = re.findall("(?<=Country: )(.*?)(?=\\n)",extract)[0]
    except:
        country = ""

    try:
        internship = re.findall("(?<=Internships\\n)(.*?)(\\n)",extract)[0][0]
    except:
        internship = ""    

    try:
        capstone = re.findall("(?<=Capstone Project\\n)(.*?)(\\n)",extract)[0][0]
    except:
        capstone = ""    

    student_details.append([url,country,internship,capstone])

    return student_details



data = pd.read_csv('/home/venkat/Downloads/MIDS/out.csv',header=None)

student_url = data[1]

for i in student_url:
    get_details(i)

with open("details.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(student_details)