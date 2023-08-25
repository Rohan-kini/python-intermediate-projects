import requests
import json

def title():
    title = "NEWS FETCHER: Get Top Headlines from Around the World with Python"
    border = " * " * (20) 

    print(border)
    print(f"{title}")
    print(border)



def fetchnews(country, category, api_key):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
    response = requests.get(url)
    return json.loads(response.text)#helps load into a dictionary

def displaynews(articles):
    for idx, article in enumerate(articles, start=1):
        print(f"News Article {idx}:")
        print("Title:", article.get('title', 'N/A'))
        print("Source:", article.get('source', {}).get('name', 'N/A'))
        print("Author:", article.get('author', 'N/A'))
        print("Published At:", article.get('publishedAt', 'N/A'))
        print("Description:", article.get('description', 'N/A'))
        print("URL:", article.get('url', 'N/A'))
        print("-" * 50)

def main():
    country =input("Which country's news would you like to explore? ")
    category =input("Please input the category of news you're looking for: ")
    api_key =input("Your API_key-",) # provide your api_key here..get it from newsApi website..

    newsdict = fetchnews(country, category, api_key)

    if newsdict['status'] == 'ok':
        articles = newsdict['articles']
        displaynews(articles)
    else:
        print("Error fetching news data.")

if __name__ == "__main__":
    title()
    main()
