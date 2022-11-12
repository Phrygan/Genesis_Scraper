import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

user_info = []
with open("credentials.txt", "rt") as credentials:
    for line in credentials:
        user_info.append(line[0:-1])

requests.packages.urllib3.disable_warnings()

with requests.Session() as s:
    payload = {
        'idTokenString': '',
        'j_username': user_info[0],
        'j_password': user_info[1],
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    p = s.post('https://students.livingston.org/livingston/j_security_check', data=payload, verify=False, headers=headers)

    payload = {
        'tab1': 'studentdata',
        'tab2': 'gradebook',
        'action': 'form',
        'studentid': '247434'
    }
    
    grades = s.get('https://students.livingston.org/livingston/parents?tab1=studentdata&tab2=gradebook&action=form&studentid=247434', data=payload, headers=headers)
    soup = BeautifulSoup(grades.text, 'html.parser')
    with open('test.html', 'w') as f:
        f.write(soup.prettify())
        
    grade_values = soup.find_all(text="%")
    for grade in grade_values:
        print(grade_values.parent)
    
    