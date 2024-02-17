from bs4 import BeautifulSoup
from urllib.request import urlopen

class MediaCrawler:
    def __init__(self):
        self.root_url = "https://media.naver.com/press/"
        self.media_list: List[Media] = []

    def init_media(self):
        root_html = urlopen(self.root_url)
        bs = BeautifulSoup(root_html, "html.parser")
        a_list = bs.find(class_="press_list_only").find_all('a')
        media_url_list = [i['href'] for i in a_list]

        # Create Media List
        for url in media_url_list:
            html = urlopen(url)
            bs = BeautifulSoup(html, "html.parser")
            title = bs.find(class_="press_hd_name").text.strip()
            self.media_list.append(Media(title,url))

    def run(self) -> None:
        # not run
        self.init_media()


    def test(self):
        for i in self.media_list:
          print(i.title)

class Media:
    def __init__(self, name, url):
        self.title = name
        self.url = url
        self.headline_list = None


class Media_content:
    def __init__(self):
        pass


m2 = MediaCrawler()
m2.run()
m2.test()
