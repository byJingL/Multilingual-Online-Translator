import requests
from bs4 import BeautifulSoup


def google_search(query, num):
    search_info = {
        'q': query,
        'num': num
    }
    r = requests.get('https://google.com/search', params=search_info)
    return r


response = google_search('Python', 10)

print(response.url)
# https://consent.google.com/ml?continue=https://www.google.com
# /search%3Fq%3DPython%26num%3D1&gl=GB&m=0&pc=srp&uxe=none&hl=en&src=1
print(response)  # <Response [200]>
print(response.status_code)  # 200
print(response.encoding)  # utf-8
print(type(response.text))  # <class 'str'>
print(type(response.content))  # <class 'bytes'>

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print('============')
for a in links:
    print(a.getText)
    print(a.text)
    print(a.get('href'))
'''
<bound method PageElement.get_text of <a href="https://policies.google.com/terms?hl=en&amp;utm_source=ucb">Terms of Service</a>>
Terms of Service
https://policies.google.com/terms?hl=en&utm_source=ucb
'''



