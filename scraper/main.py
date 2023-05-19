import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

  # Get news from exame.com
  baseUrl = 'https://exame.com'
  url = f'{baseUrl}/tecnologia/ultimas-noticias/'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # Get link of news
  links = []
  newsItems = soup.find_all('div', class_='sc-9123c2e8-0 iWjLyi')

  for item in newsItems:
    h2 = item.find('h2', class_='sc-c4a67c2e-1 ftIIQp')

    if h2 is not None:
      a = h2.find('a')
      links.append(a['href'])

  # Get content of news
  for link in links:
    newsUrl = f'{baseUrl}{link}'
    newsResponse = requests.get(newsUrl)
    newsSoup = BeautifulSoup(newsResponse.text, 'html.parser')

    newsTitleSection = newsSoup.find('section', class_='sc-f4d814da-1 idjPSz')

    if newsTitleSection is not None:
      newsTitle = newsTitleSection.find('h1')
      newsSubTitle = newsTitleSection.find('h2')

      if newsTitle is not None:
        with open('news.txt', 'a') as file:
          file.write(newsTitle.text)
          file.write('\n')
      
      if newsSubTitle is not None:
        with open('news.txt', 'a') as file:
          file.write(newsSubTitle.text)
          file.write('\n')

    newsBody = newsSoup.find('div', id='news-body')

    if newsBody is not None:
      paragraphs = newsBody.find_all('p')

      for p in paragraphs:
        with open('news.txt', 'a') as file:
          file.write(p.text)
          file.write('\n')

      with open('news.txt', 'a') as file:
        file.write('\n')
        file.write('\n') 
  
        