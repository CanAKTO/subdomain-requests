import requests as re

def make_re(url):
    try:
        return re.get(url)
    except re.exceptions.ConnectionError:
        pass


target_input ="google.com"
with open("list.txt","r") as liste:
    for word in liste:
        word = word.strip()
        #boşlukları siler veya (",.gtr") dersek bunları siler
        url = "http://"+word+"."+target_input
        response= make_re(url)
        #geri bildirim alma komutu
        if response != None:
            print(url)

