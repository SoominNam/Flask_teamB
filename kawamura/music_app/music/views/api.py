import os
import pprint
import time
import urllib.error
import urllib.request
import urllib
import json



def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

url = 'http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/wa/wsSearch?term=theoralcigarettes'
dst_path = '/home/matcha-23training/Python/Flask_teamB/kawamura/music_app/music/models/memofile/1.json'

download_file(url, dst_path)
with open('/home/matcha-23training/Python/Flask_teamB/kawamura/music_app/music/models/memofile/1.json',mode='r') as f:
    s = json.load(f)
    print(s['results'][0]['artistName'])
    print(s['results'][0]['trackName'])