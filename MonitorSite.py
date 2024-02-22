import requests
from bs4 import BeautifulSoup
page = ""

# print(page.status_code)
# print(page.content)
def verificar_site():

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        page = requests.get('https://site.com.br', headers=headers)

        soup = ""
        
        soup = BeautifulSoup(page.content, 'html.parser')
        #alinhamento de tags para análise
        # print(soup.prettify())

        table = soup.findAll('span', attrs = { 'class' : 'elementor-button-text'})
        if(len(table) > 0):
            return True
        else:
            return False
    except:
        return False


# print(monitor[1])

# print(monitor[1])
# import requests
# from bs4 import BeautifulSoup

# url = requests.get('http://10.239.83.210/4sensor.htm')

# soup = BeautifulSoup(url.content, 'html.parser')

# result = soup.find_all('td')[1].get_text()

# print(result)

