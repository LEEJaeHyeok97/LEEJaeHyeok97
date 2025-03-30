import feedparser, time

URL = "https://icecupregular.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

introduce_text = """
## Hi, God bless us 👋
Hi, I'm JaeHyeok Lee, a dev writing backend developer! passionate about making engaging experiences
"""

markdown_text = """
## 📬 Latest Blog Posts
"""  # list of blog posts will be appended here

boj_tier = """
## [![](https://mazassumnida.wtf/api/mini/generate_badge?boj=hazardous10)](https://solved.ac/hazardous10/)
![](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fohksj77&count_bg=%2329B0C6&title_bg=%23434343&icon=&icon_color=%23E7E7E7&title=&edge_flat=false)
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(introduce_text)
f.write(markdown_text)
f.write(boj_tier)
f.close()



