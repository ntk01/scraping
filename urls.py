import requests
import bs4

url_list = []


def get_urls(query):
    ua = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }
    response = requests.get('https://www.google.co.jp/search?num=10&q=' + query + '&gl=jp&hl=ja', headers=ua)
    if response.status_code != "404":

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        link = soup.select(".r > a")

        for i in range(len(link)):
            url_text = link[i].get("href").replace("/url?q=", "")
            if "https://translate.google.co.jp/" not in url_text:
                if "https://hatenablog.com/" not in url_text:
                    if "https://www.facebook.com/" not in url_text:
                        if "https://twitter.com/" not in url_text:
                            if "https://www.amazon.co.jp" not in url_text:
                                url_list.append(url_text)
                                del url_list[:-10]
    return url_list