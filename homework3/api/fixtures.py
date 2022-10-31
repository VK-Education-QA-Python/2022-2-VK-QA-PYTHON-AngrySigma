import os.path
from os import getenv
from random import choice, randint

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
def credentials():
    email = getenv('EMAIL')
    password = getenv('PASSWORD')
    return email, password


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return randint(0, 10000)


@pytest.fixture(scope='function')
def segment_data(faker):
    first_param = choice(['positive', 'negative'])
    second_param = choice(['positive', 'negative'])
    data = (f'{{"name":"{faker.company()}",'
            '"pass_condition":1,'
            '"relations":'
            '[{"object_type":"remarketing_player",'
            f'"params":{{"type":"{first_param}",'
            f'"left":{randint(1, 365)},'
            '"right":1}},'
            '{"object_type":"remarketing_payer",'
            f'"params":{{"type":"{second_param}",'
            f'"left":{randint(1, 365)},'
            '"right":1}}],'
            '"logicType":"or"}')
    return data


@pytest.fixture(scope='function')
def vk_group_data(object_id=115340687):
    data = f'{{"object_id": {object_id}}}'
    return data


@pytest.fixture(scope='function')
def vk_group_segment_data(faker):
    first_param = 115340687
    second_param = choice(['positive', 'negative'])
    data = ('{"name":"asdfasdf",'
            '"pass_condition":1,'
            '"relations":'
            '[{"object_type":"remarketing_vk_group",'
            f'"params":{{"source_id":{first_param},'
            f'"type":"{second_param}"}}}}],'
            '"logicType":"or"}')
    return data


@pytest.fixture()
def image_path(repo_root):
    return os.path.join(repo_root, 'files', 'image.png')
