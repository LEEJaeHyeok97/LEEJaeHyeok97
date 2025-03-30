import feedparser, time

URL = "https://icecupregular.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## Hi, I'm JaeHyeok Lee, a dev writing backend developer! passionate about making engaging experiences
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()


[![Solved.ac
프로필](http://mazassumnida.wtf/api/generate_badge?boj={handle})](https://solved.ac/{hazardous10})
