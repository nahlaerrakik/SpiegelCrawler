__author__ = 'nahla.errakik'

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from crawler.settings import DB


db_string = r'postgresql+psycopg2://{}:{}@{}/{}'.format(DB['user'], DB['password'], DB['host'], DB['name'])

Engine = create_engine(db_string)
Session = sessionmaker(bind=Engine)
Base = declarative_base()


@contextmanager
def session_scope():
    """Manages database session scope"""
    s = Session()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()


def session(func):
    """Decorator used for CRUD operations on the database"""
    def wrapper(*args, **kwargs):
        with session_scope() as s:
            func(s=s, *args, **kwargs)

    return wrapper
