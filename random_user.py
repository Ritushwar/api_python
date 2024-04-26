import requests
def FetchRandomUser():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name, country
    else:
        raise Exception("Failed To Fetch User Data")

def main():
    try:
        User_Name, Country = FetchRandomUser()
        print(f"Username: {User_Name} \n Country: {Country}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()
    