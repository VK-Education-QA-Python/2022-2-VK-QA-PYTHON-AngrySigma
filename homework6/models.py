from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR, VARCHAR

Base = declarative_base()


class PopularRequestsModel(Base):
    __tablename__ = 'popular_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.num} requests to {self.url}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(500), nullable=False)
    num = Column(Integer, nullable=False, default=0)


class RequestMethodsModel(Base):
    __tablename__ = 'request_methods'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.method} requests: {self.num}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(VARCHAR(10), nullable=False)
    num = Column(Integer, nullable=False, default=0)


class IpModel(Base):
    __tablename__ = 'users_caused_500'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.num} requests from {self.ip}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(CHAR(15), nullable=False)
    num = Column(Integer, nullable=False, default=0)


class RequestsTotalModel(Base):
    __tablename__ = 'requests_total'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Total number of requests: {self.num}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num = Column(Integer, nullable=False, default=0)


class Requests400Model(Base):
    __tablename__ = 'requests_caused_400'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return (f'IP: {self.ip}, '
                f'URL: {self.url}, '
                f'status code: {self.status_code}, '
                f'bytes sent: {self.bytessent}')

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(CHAR(15), nullable=False)
    url = Column(VARCHAR(500), nullable=False)
    status_code = Column(Integer, nullable=False)
    bytessent = Column(Integer, nullable=False)
