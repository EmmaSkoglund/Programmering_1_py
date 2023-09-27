import requests
#200 = ok

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)

artists = r.json()
print(artists)

artists_list = artists["artists"]
print(artists_list)

print("-- ARTIST DB --")
for artist in artists_list:
    print(artist["name"])
print("------------------")
print("Select artist: ")
artist_name = input("> ")
artist_name = artist_name.title()
print("------------------")
print(artist_name)
print("******************")

# Hämta id för en specifik artist
for artist in artists_list:
    try:
        if artist_name == artist["name"]:
            artist_id = artist["id"]
            print(artist_id)
            break
    except NameError:
        print("Artist saknas!")
        exit(1)

# Hämta info
url = url + artist_id
r = requests.get(url)
artist_info = r.json()
artist_info = artist_info["artist"]

print("Genres:", "," .join(artist_info["genres"]))
print("Years active: ", "," .join(artist_info["years active "]))
print("Members: ", "," .join(artist_info["menbers"]))


