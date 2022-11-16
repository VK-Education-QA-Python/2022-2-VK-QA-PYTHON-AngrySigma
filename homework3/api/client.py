from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiServerException(Exception):
    pass


class ApiClient:
    def __init__(self, base_url, auth_url, email=None, password=None):
        self.base_url = base_url
        self.auth_url = auth_url
        self.session = requests.Session()
        self.email = email
        self.password = password
        if not self.session.get(self.base_url).status_code == 200:
            raise ApiServerException(f'Did not get code 200 from {base_url}')

    def post_login(self, email=None, password=None):
        if email is None:
            email = self.email
        if password is None:
            password = self.password
        data = {
            'email': email,
            'password': password,
            'continue':
                f'{self.base_url}/csrf/'
        }
        headers = {
            'Referer': self.base_url,
        }
        self.session.post(self.auth_url,
                          data=data, headers=headers)
        assert self.session.cookies['csrftoken']

    def _request(self, method, location, headers=None, data=None):
        url = urljoin(self.base_url, location)
        response = self.session.request(method=method,
                                        url=url,
                                        headers=headers,
                                        data=data)
        return response

    def create_segment(self, segment_data):
        headers = self.csrf_token
        response = self._request(method='POST',
                                 location='/api/v2/remarketing/segments.json',
                                 headers=headers,
                                 data=segment_data)
        return response.json()['id']

    def delete_segment(self, id):
        headers = self.csrf_token
        self._request(method='DELETE',
                      location=f'/api/v2/remarketing/segments/{id}.json',
                      headers=headers)

    def get_segment(self, id):
        headers = self.csrf_token
        response = self._request(method='GET',
                                 location=(f'/api/v2/remarketing/'
                                           f'segments/{id}.json'),
                                 headers=headers)
        if response.status_code != 200:
            raise ResponseStatusCodeException(
                'Did not get segment object from server')
        return response.json()

    def add_vk_group(self, data):
        headers = self.csrf_token
        response = self._request(method='POST',
                                 location='/api/v2/remarketing/vk_groups.json',
                                 headers=headers,
                                 data=data)
        if response.status_code != 201:
            raise ResponseStatusCodeException(
                'Did not get status 201_CREATED from server')
        return response.json()

    def get_vk_groups(self):
        headers = self.csrf_token
        response = self._request(method='GET',
                                 location='/api/v2/remarketing/vk_groups.json',
                                 headers=headers)
        if response.status_code != 200:
            raise ResponseStatusCodeException(
                'Did not get segment object from server')
        return response.json()

    def delete_vk_group(self, group_id):
        headers = self.csrf_token
        response = self._request(
            method='DELETE',
            location=f'/api/v2/remarketing/vk_groups/{group_id}.json',
            headers=headers)
        if response.status_code != 204:
            raise ResponseStatusCodeException(
                'Did not get deletion confirmation from server')

    def upload_image(self, image):
        headers = self.xcsrf_header().update({'Content-Type': 'multipart/form-data'})
        response = self._request(
            method='POST',
            location='/api/v2/content/static.json',
            headers=headers,
            data=f'{{"file": "{image}", "data": {{"width": 1000, "height": 1000}}}}')
        if response.status_code != 201:
            raise ResponseStatusCodeException()
        return response.json()


