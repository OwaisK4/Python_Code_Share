import requests

# f = open("input_binary.txt", "wb")

# name = ["Owais", "Ali", "Khan"]
# for i in name:
#     f.write("\n")

# f.close()

url = "https://vgmsite.com/soundtracks/kara-no-shoujo-original-soundtrack/vtrqyrcgyg/1-01%20-%20Azure%20Bird.mp3"
mp3file = requests.get(url)
print(mp3file.status_code)

filename = "song.mp3"
f = open(f"{filename}", "wb")
f.write(mp3file.content)
f.close()
