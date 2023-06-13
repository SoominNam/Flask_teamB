from flask import request, redirect, url_for, render_template, flash, session
from music import app
from music import db
from music.models.database import Music
from datetime import date,datetime
import urllib.error
import urllib.request
import urllib
import json

# @app.route('/update_delete_entry', methods=['POST'])
# def update_delete_entry():
#     if request.form["button"] == "insert":
#         id_count = Music.query.count() + 1
#         entry = Music(
#             id = id_count,
#             band_name = request.form['artist'],
#             music_name = request.form['music']
#         )
#         db.session.add(entry)
#         db.session.commit()
#         flash('アーティストと楽曲が登録されました')
#         return render_template('result.html', entry=entry, result="登録") 
#     if request.form["button"] == "delete":
#         date_count = Music.query.filter_by(band_name = request.form['artist'],music_name = request.form['music']).count()
#         if request.form['artist'] == '' or request.form['music'] == '':
#             flash('入力してください')
#             return render_template('input.html')
#         if date_count == 0:
#             flash(request.form['artist']+'の'+request.form['music']+'は登録されていません')
#             return render_template('input.html')
#         else:
#             entry = Music.query.filter_by(band_name = request.form['artist'],music_name = request.form['music']).first()
#             db.session.delete(entry)
#             db.session.commit()
#             flash('楽曲が削除されました')
#             return render_template('result.html', entry=entry, result="削除")


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

@app.route('/search', methods=['POST'])
def search():
    if request.form['music']=='':
        url = 'http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/wa/wsSearch?term='+ request.form['artist']
        dst_path = '/home/matcha-23training/Python/Flask_teamB/kawamura/music_app/music/models/memofile/1.json'
        download_file(url, dst_path)
        with open(dst_path,mode='r') as f:
            s = json.load(f)
            result = []
            album = []
            urls=[]
            for  i in s['results']:    
                result.append(i['trackName'])
                album.append(i['collectionName'])
                urls.append(i['trackViewUrl'])
        return render_template('search_music.html', results=result,album=album,urls=urls)
    if request.form['artist']=='':
        url = 'http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/wa/wsSearch?term='+ request.form['music']
        dst_path = '/home/matcha-23training/Python/Flask_teamB/kawamura/music_app/music/models/memofile/1.json'
        download_file(url, dst_path)
        with open(dst_path,mode='r') as f:
            s = json.load(f)
            result = []
            for  i in s['results']:
                result.append(i['artistName'])
        return render_template('search_music.html', results=result)


    
            #print(s['results'][i]['trackName'])
    # if request.form['music'] == "":
    #     result = Music.query.filter_by(band_name = request.form['artist']).all()
    #     return render_template('search.html', result=result)
    # if request.form['artist'] == "":
    #     result = Music.query.filter_by(music_name = request.form['music']).all()
    #     return render_template('search_music.html', result=result)
       
