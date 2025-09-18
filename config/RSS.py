import feedparser
## https://www.dailysecu.com/rss/S1N2.xml
## http://www.boannews.com/media/news_rss.xml?skind=6

## 데일리시큐 이슈
def dailySecure():
    rss_url = "https://www.dailysecu.com/rss/S1N2.xml"
    feed = feedparser.parse(rss_url)

    return feed

## 보안 정책
def sercureRule():
    rss_url = "http://www.boannews.com/media/news_rss.xml?skind=6"
    feed = feedparser.parse(rss_url)

    return feed