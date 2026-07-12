import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

def crawl(url):
    urls = set()
    domain_name = urlparse(url).netloc
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for a_tag in soup.find_all("a"):
        href = a_tag.get("href")
        if not href:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            continue
        if href in urls:
            continue
        if domain_name not in href:
            continue
        urls.add(href)

    return urls

start_url = input("Enter URL: ").strip()
found_links = crawl(start_url)

print(f"Found {len(found_links)} links:")
for link in list(found_links)[:10]:
    print(link)
