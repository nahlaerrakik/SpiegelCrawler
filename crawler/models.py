__author__ = 'nahla.errakik'

from datetime import datetime

from sqlalchemy import Column, String, TEXT, DateTime

from . import Base, Engine, session


class Article(Base):
    """ Model class for articles table where articles will be stored in the database """
    __tablename__ = 'articles'

    article_id = Column(String, primary_key=True, nullable=False)
    title = Column(String)
    subtitle = Column(String)
    abstract = Column(TEXT)
    download_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now())

    def __init__(self, article_id, title, subtitle, abstract):
        self.article_id = article_id
        self.title = title
        self.subtitle = subtitle
        self.abstract = abstract

    @session
    def insert(self, s):
        s.add(self)

    @session
    def update(self, s):
        article = s.query(Article).filter_by(article_id=self.article_id).first()
        if article is None:
            return

        article.update_time = datetime.now()


Base.metadata.create_all(Engine)
