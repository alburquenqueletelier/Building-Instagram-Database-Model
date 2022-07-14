import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_like_post = Table('association_like_post', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('post_id', ForeignKey('post.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    nacimiento = Column(String(250), nullable=False)
    lista_seguidores = relationship("Seguidores", back_populates="user")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship("Comment")
    likes = relationship(
        "Post",
        secondary=association_like_post,
        back_populates="users_like")

    
class Seguidores(Base):
    __tablename__ = 'lista_seguidores'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="lista_seguidores")


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship("Comment")
    users_like = relationship(
        "User",
        secondary=association_like_post,
        back_populates="user")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e