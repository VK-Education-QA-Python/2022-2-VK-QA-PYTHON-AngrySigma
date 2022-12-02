import pytest
from models import (PopularRequestsModel,
                    RequestMethodsModel,
                    IpModel,
                    RequestsTotalModel,
                    Requests400Model)
from parser import (popular_requests,
                    request_methods,
                    users_caused_500,
                    count_requests,
                    requests_caused_400)


class MyTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client = mysql_client

    def get_filtered_model(self, model, **filters):
        self.client.session.commit()
        return self.client.session.query(model).filter_by(
            **filters).all()

    def count_requests_caused_400(self):
        self.client.session.commit()
        return self.client.session.query(Requests400Model).count()

    def count_rows(self, model):
        self.client.session.commit()
        return self.client.session.query(model).count()

    def get_total_requests(self):
        self.client.session.commit()
        return self.client.session.query(RequestsTotalModel).all()


class TestMysql(MyTest):

    def test_popular_requests(self, logfile):
        rows_to_table = 10
        for request in popular_requests(logfile, rows_to_table).items():
            self.client.create_request(*request)
        assert self.count_rows(PopularRequestsModel) == rows_to_table
        assert self.get_filtered_model(PopularRequestsModel,
                                       url='/administrator/index.php HTTP/1.1',
                                       num=103849)

    def test_request_methods(self, logfile):
        for method in request_methods(logfile).items():
            self.client.create_request_method(*method)
        assert self.count_rows(RequestMethodsModel) == 9
        assert self.get_filtered_model(RequestMethodsModel,
                                       method='GET',
                                       num=122096)

    def test_users_caused_500(self, logfile):
        rows_to_table = 5
        for ip in users_caused_500(logfile, rows_to_table).items():
            self.client.create_ip(*ip)
        assert self.count_rows(IpModel) == rows_to_table
        assert self.get_filtered_model(IpModel, ip='189.217.45.73', num=225)

    def test_requests_total(self, logfile):
        self.client.create_requests_total(count_requests(logfile))
        assert self.get_total_requests()[0].num == 225133

    def test_requests_caused_400(self, logfile):
        rows_to_table = 5
        for request in requests_caused_400(logfile, rows_to_table).items():
            self.client.create_request_400(*request)
        assert self.count_rows(Requests400Model) == rows_to_table
        assert self.get_filtered_model(Requests400Model,
                                       ip='164.132.159.94',
                                       status_code=404,
                                       bytessent=442,
                                       id=1)
