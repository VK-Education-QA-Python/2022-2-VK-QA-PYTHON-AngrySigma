import argparse
import json
import os.path
import re
from collections import OrderedDict
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true')
jsonify = parser.parse_args().json

urls = dict()

with open(os.path.dirname(__file__) + '/../access.log', 'r') as logfile:
    line = logfile.readline()
    while line:
        url = re.match(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
            r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})'
            r'\] \"(.*('
            r'(?P<method>GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)'
            r').* (?P<url>.+HTTP\/1\.[10]))" (?P<statuscode>\d{3}) '
            r'(?P<bytessent>\d+|-) (["](?P<refferer>(\-)|(.+))["]) '
            r'(["](?P<useragent>.+)["])',
            line).group('url')
        if url in urls:
            urls[url] += 1
        else:
            urls[url] = 1
        line = logfile.readline()

urls = OrderedDict(list(dict(sorted(urls.items(),
                             key=lambda item: item[1],
                             reverse=True)).items())[:10])

if jsonify:
    with open('popular_requests.json', 'w') as f:
        json.dump(urls, f)
else:
    pprint(urls)
