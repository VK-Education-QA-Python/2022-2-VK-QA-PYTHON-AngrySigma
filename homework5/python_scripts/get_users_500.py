import argparse
import json
import os.path
import re
from collections import OrderedDict
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true')
jsonify = parser.parse_args().json

ips = dict()

with open(os.path.dirname(__file__) + '/../access.log', 'r') as logfile:
    line = logfile.readline()
    while line:
        ip = re.match(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
            r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})'
            r'\] \"(.*('
            r'(?P<method>GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)'
            r').* (?P<url>.+)(HTTP\/1\.[10]))" '
            r'(?P<statuscode>5\d{2}) (?P<bytessent>\d+|-) '
            r'(["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])', line)
        if ip:
            if ip.group('ip') in ips:
                ips[ip.group('ip')] += 1
            else:
                ips[ip.group('ip')] = 1
        line = logfile.readline()

ips = OrderedDict((list(dict(sorted(ips.items(),
                             key=lambda item: item[1],
                             reverse=True)).items())[:5]))
if jsonify:
    with open('users_500.json', 'w') as f:
        json.dump(ips, f)
else:
    pprint(ips)
