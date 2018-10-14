from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR056T1hFU0FuWnBLQUFQAQ?hl=vi&gl=VN&ceid=VN%3Avi"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
	print(news.title.text)
	print(news.link.text)
	print(news.pubDate.text)
	print("-" * 60)
