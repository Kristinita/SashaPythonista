import re
import urllib

from bs4 import BeautifulSoup

from w3lib.url import safe_url_string


# ASCII link for solved encoding problems —
# http://stackoverflow.com/a/40654295/5951529
ascii_link = safe_url_string(
    u'http://duckduckgo.com/html/?q=' + 'Поиск Кристиниты',
    encoding="UTF-8")
print(ascii_link)
# SERP DuckDuckGo
serp = urllib.request.urlopen(ascii_link)
# Reading SERP
read_serp = serp.read()
# BeautifulSoup — http://stackoverflow.com/a/11923803/5951529
parsed = BeautifulSoup(read_serp, "lxml")
# Parsed first link
first_link = parsed.findAll(
    'div', {'class': re.compile('links_main*')})[0].a['href']
# Remove DuckDuckGo specific characters —
# http://stackoverflow.com/a/3942100/5951529
remove_duckduckgo_symbols = first_link.replace("/l/?kh=-1&uddg=", "")
# http://stackoverflow.com/a/32451970/5951529
final_link = (urllib.parse.unquote(remove_duckduckgo_symbols))
# Markdown link
markdown_link = '[' + 'Поиск Кристиниты' + ']' + \
    '(' + final_link + ')'

print(markdown_link)
