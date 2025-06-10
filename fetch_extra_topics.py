import requests
from bs4 import BeautifulSoup

def crawl_naver_topics():
    try:
        r = requests.get("https://news.naver.com/main/ranking/popularDay.naver", timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        titles = soup.select(".rankingnews_box .list_title")
        return [t.text.strip() for t in titles[:10]]
    except:
        return []

def crawl_daum_keywords():
    try:
        r = requests.get("https://www.daum.net", timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        return [t.text.strip() for t in soup.select(".link_issue")][:10]
    except:
        return []

def crawl_blog_topics():
    try:
        r = requests.get("https://www.tistory.com", timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        h3_tags = soup.select("h3")
        return [tag.text.strip() for tag in h3_tags if len(tag.text.strip()) > 10][:5]
    except:
        return []

def get_extra_topics():
    return (
        crawl_naver_topics() +
        crawl_daum_keywords() +
        crawl_blog_topics()
    )
