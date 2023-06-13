import sys
from sqlalchemy import Column, String, Date, Integer
from holiday import db

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key = True)
    holi_text = Column('holi_text',String(20))
