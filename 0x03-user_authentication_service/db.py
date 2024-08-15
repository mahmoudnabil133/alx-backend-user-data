#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        "add user to db"
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs):
        "find user"
        session = self._session
        user_attributes = {'id', 'email', 'hashed_password',
                           'session_id', 'reset_token'}

        invalid_attrs = set(kwargs) - user_attributes
        if invalid_attrs:
            raise InvalidRequestError()
        for k in kwargs:
            if k not in user_attributes:
                raise InvalidRequestError
        matched_users = session.query(User).filter_by(**kwargs).first()
        if not matched_users:
            raise NoResultFound()
        return matched_users
