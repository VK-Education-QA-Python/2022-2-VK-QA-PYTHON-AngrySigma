import base64
from os import getenv
from http import HTTPStatus

import pytest
from dotenv import load_dotenv

from api.base import ApiBase
from api.client import ResponseStatusCodeException


class TestApiAuth(ApiBase):
    authorize = False

    @pytest.mark.API
    def test_login(self):
        self.api_client.post_login()
        assert self.api_client.session.get('https://target-sandbox.my.com/'
            'api/v2/campaigns.json').status_code == HTTPStatus.OK

    @pytest.mark.API
    def test_negative_login(self):
        load_dotenv()
        self.api_client.session.cookies.clear()
        with pytest.raises(KeyError):
            self.api_client.post_login(email=getenv('WRONG_EMAIL'),
                                       password=getenv('WRONG_PASSWORD'))
        assert self.api_client.session.get('https://target-sandbox.my.com/'
            'api/v2/campaigns.json').status_code == HTTPStatus.UNAUTHORIZED


class TestApi(ApiBase):
    @pytest.mark.skip
    def test_campaign_creation(self, image_path):
        with open(image_path, 'rb') as f:
            image = base64.b64encode(f.read())
        self.api_client.upload_image(image)

    @pytest.mark.API
    def test_segment_creation(self, segment_data):
        segment_id = self.api_client.create_segment(segment_data)
        assert self.api_client.get_segment(segment_id).get('id') == segment_id
        self.api_client.delete_segment(segment_id)
        with pytest.raises(ResponseStatusCodeException):
            self.api_client.get_segment(segment_id)

    @pytest.mark.API
    def test_segment_creation_from_vk_ok(self,
                                         vk_group_data,
                                         vk_group_segment_data):
        group_id = self.api_client.add_vk_group(vk_group_data).get('id')
        response = self.api_client.get_vk_groups()
        assert [group for group in response['items']
                if group['id'] == group_id]

        segment_id = self.api_client.create_segment(vk_group_segment_data)
        assert self.api_client.get_segment(segment_id).get('id') == segment_id

        self.api_client.delete_segment(segment_id)
        with pytest.raises(ResponseStatusCodeException):
            self.api_client.get_segment(segment_id)

        self.api_client.delete_vk_group(group_id)
        response = self.api_client.get_vk_groups()
        assert not [group for group in response['items']
                    if group['id'] == group_id]
