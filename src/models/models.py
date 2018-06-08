from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'Artist'
    stageName = Column(String(40), primary_key=True)
    name = Column(String(30))
    lastName = Column(String(30))
    age = Column(Integer())

class AudioFile(Base):
    __tablename__ = 'AudioFile'
    filename = Column(String(100), primary_key=True)
    isAudioFile = Column(Boolean(False))

class AudioFileByArtist(Base):
    __tablename__ = 'AudioFileByArtist'
    artist = Column(String(40), ForeignKey('Artist.stageName',ondelete='CASCADE'),primary_key=True)
    filename = Column(String(100),ForeignKey('AudioFile.filename',ondelete='CASCADE'),primary_key=True)
    uploaded = Column(DateTime, default=func.now())

class User_Data(Base):
    __tablename__ = 'User_Data'
    userName = Column(String(50), primary_key=True)
    name = Column(String(40))
    lastName = Column(String(40))
    age = Column(Integer())

class User_Login(Base):
    __tablename__ = 'User_Login'
    userName = Column(String(50), ForeignKey('User_Data.userName',ondelete='CASCADE'),primary_key=True)
    password = Column(String(128))
    lastPassChange = Column(DateTime, default=func.now())

class Album(Base):
    __tablename__ = 'Album'
    name = Column(String(30), primary_key=True)
    genre = Column(String(30))
