import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Base
from models import (PopularRequestsModel,
                    RequestMethodsModel,
                    IpModel,
                    RequestsTotalModel,
                    Requests400Model)


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = '3306'
        self.password = password
        self.host = '127.0.0.1'
        self.db_name = db_name
        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = (f'mysql+pymysql://{self.user}:{self.password}'
               f'@{self.host}:{self.port}/{db}')
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def create_table(self, name):
        if not sqlalchemy.inspect(self.engine).has_table(name):
            Base.metadata.tables[name].create(self.engine)

    def create_request(self, url=None, num=0):
        request = PopularRequestsModel(url=url, num=num)
        self.session.add(request)

    def create_request_method(self, method=None, num=0):
        request = RequestMethodsModel(method=method, num=num)
        self.session.add(request)

    def create_ip(self, ip=None, num=0):
        ip = IpModel(ip=ip, num=num)
        self.session.add(ip)

    def create_requests_total(self, num=0):
        total = RequestsTotalModel(num=num)
        self.session.add(total)

    def create_request_400(self, datatuple, bytessent=0):
        request = Requests400Model(ip=datatuple[0],
                                   status_code=datatuple[1],
                                   url=datatuple[2],
                                   bytessent=bytessent)
        self.session.add(request)

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()
