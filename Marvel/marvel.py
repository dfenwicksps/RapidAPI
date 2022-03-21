import requests, time, hashlib

timestamp = str(time.time())
publickey = "c6ed190a2ede12009ea83d486bab3954"
privatekey = "57b14eac0cfffc30296fa7c4324f9e3054beb52e"
hash_string = timestamp + privatekey + publickey  #adding the string together for hashing
hash = hashlib.md5(hash_string.encode("utf-8")).hexdigest()
parameters = {"ts": timestamp, "apikey": publickey, "hash": hash}

url = "http://gateway.marvel.com/v1/public/comics/1111"
request = requests.get(url, params=parameters)
print(request.status_code)

#request = requests.get(url, params=parameters, proxies=None, auth=proxy_auth).json()
request = requests.get(url, params=parameters).json()

print(request)  # to display all the wrapper and container data
print(request["data"]["results"])  # displays comic data only
print(request["data"]["results"][0]["title"])  # displays the title of the first comic result
