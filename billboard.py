import requests
from bs4 import BeautifulSoup

def get_billboard_hot_100(year):
    date = f"{year}-01-01"
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    song_tags = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
    songs = []
    for tag in song_tags:
        song_text = tag.get_text().strip()
        songs.append(song_text)
    return songs

year = input("Enter a year (YYYY): ")
print(get_billboard_hot_100(year))
