import argparse
import json
import os.path
import re
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true')
jsonify = parser.parse_args().json

request_types = {'GET': 0,
                 'HEAD': 0,
                 'POST': 0,
                 'PUT': 0,
                 'DELETE': 0,
                 'CONNECT': 0,
                 'OPTIONS': 0,
                 'TRACE': 0,
                 'PATCH': 0}

with open(os.path.dirname(__file__) + '/../access.log', 'r') as logfile:
    line = logfile.readline()
    while line:
        log = re.match(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
            r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} '
            r'(\+|\-)\d{4})\] \"(.*('
            r'(?P<method>GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)'
            r').* (?P<url>.+)(HTTP\/1\.[10]))" (?P<statuscode>\d{3}) '
            r'(?P<bytessent>\d+|-) (["](?P<refferer>(\-)|(.+))["]) '
            r'(["](?P<useragent>.+)["])', line)
        request_types[log.group('method')] += 1
        line = logfile.readline()
if jsonify:
    with open('request_types.json', 'w') as f:
        json.dump(request_types, f)
else:
    pprint(request_types)
