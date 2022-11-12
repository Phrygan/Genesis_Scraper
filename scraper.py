import requests
from bs4 import BeautifulSoup
from lxml import etree

class Scraper:
    user_credentials = []
    dom = None


    def __init__(self):
        self.get_credentials()
        self.get_gradebook()

    def get_credentials(self):
        with open("credentials.txt", "rt") as credentials:
            for line in credentials:
                self.user_credentials.append(line[0:-1])

    def get_gradebook(self):
        s = requests.Session()
        payload = {
            'idTokenString': '',
            'j_username': self.user_credentials[0],
            'j_password': self.user_credentils[1],
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        s.post('https://students.livingston.org/livingston/j_security_check', data=payload, verify=False, headers=headers)

        payload = {
            'tab1': 'studentdata',
            'tab2': 'gradebook',
            'action': 'form',
            'studentid': '247434'
        }
        
        s.get('https://students.livingston.org/livingston/parents?tab1=studentdata&tab2=gradebook&action=form&studentid=247434', data=payload, headers=headers)
        # self.soup = BeautifulSoup(grades.content, 'html.parser')
        # with open('test.html', 'w') as f:
        #     f.write(self.soup.prettify())

        payload = {
            'tab1': 'studentdata',
            'tab2': 'gradebook',
            'tab3': 'coursesummary',
            'studentid': '247434',
            'action': 'form',
            'courseCode': '035-1',
            'courseSection': '15',
            'mp': 'MP1'
        }
        course = s.get('https://students.livingston.org/livingston/parents?tab1=studentdata&tab2=gradebook&tab3=coursesummary&studentid=247434&action=form&courseCode=035-1&courseSection=15&mp=MP1', data=payload, headers=headers)
        self.soup = BeautifulSoup(course.content, 'html.parser')
        with open('test.html', 'w') as f:
            f.write(self.soup.prettify())
        self.dom = etree.HTML(str(self.soup))
        self.get_class_grades()
        s.close()

    def get_class_grades(self):
        print(self.dom.xpath('/html')[0])
        