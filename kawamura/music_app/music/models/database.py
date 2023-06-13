from music import db
from datetime import datetime


class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column('id',db.Integer,primary_key = True)
    band_name = db.Column('band_name',db.String(20))
    music_name = db.Column('band_music',db.String(20))
    
    def __init__(self,id=None,band_name=None,music_name=None):
        self.id = id
        self.band_name = band_name
        self.music_name = music_name

    def __repr(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id,self.id,self.band_name,self.music_name)
    
