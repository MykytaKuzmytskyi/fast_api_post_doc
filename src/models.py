from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .databases import Base

# Вспомогательная таблица для связи многие-ко-многим между пользователями и группами
user_group_association = Table(
    'user_group_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Определяем отношение многие-ко-многим с моделью Group
    groups = relationship('Group', secondary=user_group_association, back_populates='users')


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Определяем отношение многие-ко-многим с моделью User
    users = relationship('User', secondary=user_group_association, back_populates='groups')
