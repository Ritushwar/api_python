import requests
import random
def get_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        index = random.randrange(5)
        quotes = data["data"]["data"][index]
        author = quotes["author"]
        contents = quotes["content"]
        return author, contents
    else:
        raise Exception("Failed to fetch code")
    
def main():
    try:
        author, contents = get_quotes()
        print(f"{contents}\n -{author}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()