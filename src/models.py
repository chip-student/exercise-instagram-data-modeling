import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    iduser = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password= Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    created= Column(DateTime, nullable=False)
    updated= Column(DateTime, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    idpost = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)
    total_like=Column(Integer, nullable=False)
    total_comment=Column(Integer, nullable=False)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    idmedia = Column(Integer, primary_key=True)
    tipo= Column(String(100), nullable=False)
    url= Column(String(300), nullable=False)
    idpost = Column(Integer, ForeignKey('post.idpost'))
    post = relationship(Post)

class Post_Like(Base):
    __tablename__ = 'post_like'
    idpostlike= Column(Integer, primary_key=True)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)
    idpost = Column(Integer, ForeignKey('post.idpost'))
    post = relationship(Post)
    created= Column(DateTime, nullable=False)
    updated= Column(DateTime, nullable=False)

class Post_Comment(Base):
    __tablename__ = 'post_comment'
    idpostcomment= Column(Integer, primary_key=True)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)
    idpost = Column(Integer, ForeignKey('post.idpost'))
    post = relationship(Post)
    comment = Column(String(200), nullable=False)
    created= Column(DateTime, nullable=False)
    updated= Column(DateTime, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')