import whois

from downloadPage import download
from downloadSitemap import crawl_sitemap

download("https://www.varzesh3.com/")
crawl_sitemap('http://example.webscraping.com/sitemap.xml')
# print(whois.whois("www.varzesh3.com"))
