import requests
from bs4 import BeautifulSoup
import json

def fetch_movie_data():
    url = "https://movie.douban.com/chart"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    movies = []
    movie_containers = soup.select("div.indent table")
    
    for container in movie_containers:
        title = container.select_one("div.pl2 a").text.strip()
        rating = container.select_one("span.rating_nums").text.strip() if container.select_one("span.rating_nums") else "N/A"
        link = container.select_one("div.pl2 a")["href"]
        
        movies.append({
            "title": title,
            "rating": rating,
            "link": link
        })
    
    # Save data to a JSON file
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    fetch_movie_data()
    print("Movies saved to movies.json")