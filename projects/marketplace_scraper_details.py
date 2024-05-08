import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/marketplace/item/1857699751414938/?ref=search&referral_code=null&referral_story_type=post&__tn__=!%3AD'

html = requests.get(url)
detailed_soup = BeautifulSoup(html.text, "html.parser")
div = detailed_soup.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u')

print(div)