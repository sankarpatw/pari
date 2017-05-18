import html2text
from collections import Counter

from article.models import Article

all_live = Article.objects.live()
all_not_live = Article.objects.not_live()

count = 0
for each in all_live:
    count += intCounter(html2text.html2text(each.content).split())

print "All live count:"
print count

count = 0
for each in all_not_live:
    count += int(Counter(html2text.html2text(each.content).split()))

print "All live count:"
print count