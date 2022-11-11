import requests
import json
from bs4 import BeautifulSoup

user_info = []
with open("credentials.txt", "rt") as credentials:
    for line in credentials:
        user_info.append(line[0:-1])



with requests.Session() as s:
    payload = {
        'idTokenString': '',
        'j_username': user_info[0],
        'j_password': user_info[1],
    }
    p = s.post('https://students.livingston.org/livingston/sis/j_security_check', data=payload, verify=False)
    print(p.url)

    r = s.get('https://students.livingston.org/livingston/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=247434&action=form')
    print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title)


# window = session.get('https://students.livingston.org/livingston/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=247434&action=form')
# soup = BeautifulSoup(window.text, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# loginurl = 'https://the-internet.herokuapp.com/authenticate'
# secure_url = 'https://the-internet.herokuapp.com/secure'

# payload = {
#     'username': 'tomsmith',
#     'password': 'SuperSecretPassword!'
# }

# r = requests.post(loginurl, data=payload)

# print(r.text)