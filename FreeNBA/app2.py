import requests

url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "bd06bb2382msh874e76e6ff29000p12bc4djsn26abdf362181"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)



#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
