import re
from collections import OrderedDict

URL_REGEX = (r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
             r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} '
             r'(\+|\-)\d{4})\] \"(.*('
             r'?P<method>GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH'
             r').* (?P<url>.+HTTP\/1\.[10]))" '
             r'(?P<statuscode>\d{3}) (?P<bytessent>\d+|-) '
             r'(["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])')


def popular_requests(logfile, number=10):
    urls = dict()
    for line in logfile:
        print(line)
        url = re.match(URL_REGEX,
                       line).group('url')
        if url in urls:
            urls[url] += 1
        else:
            urls[url] = 1

    urls = OrderedDict(list(dict(sorted(urls.items(),
                                        key=lambda item: item[1],
                                        reverse=True)).items())[:number])
    return urls


def count_requests(logfile):
    return len(logfile)


def request_methods(logfile):
    request_types = {'GET': 0,
                     'HEAD': 0,
                     'POST': 0,
                     'PUT': 0,
                     'DELETE': 0,
                     'CONNECT': 0,
                     'OPTIONS': 0,
                     'TRACE': 0,
                     'PATCH': 0}
    for line in logfile:
        log = re.match(URL_REGEX, line)
        request_types[log.group('method')] += 1
    return request_types


def users_caused_500(logfile=None, number=5):
    ips = dict()
    for line in logfile:
        ip = re.match(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
            r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} '
            r'(\+|\-)\d{4})\] \"(.*('
            r'?P<method>'
            r'GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH'
            r').* (?P<url>.+HTTP\/1\.[10]))" (?P<statuscode>5\d{2}) '
            r'(?P<bytessent>\d+|-) (["](?P<refferer>(\-)|(.+))["]) '
            r'(["](?P<useragent>.+)["])', line)
        if ip:
            if ip.group('ip') in ips:
                ips[ip.group('ip')] += 1
            else:
                ips[ip.group('ip')] = 1
    ips = OrderedDict((list(dict(sorted(ips.items(),
                                        key=lambda item: item[1],
                                        reverse=True)).items())[:number]))
    return ips


def requests_caused_400(logfile, number=5):
    urls = dict()
    for line in logfile:
        request = re.match(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \['
            r'(?P<datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} '
            r'(\+|\-)\d{4})\] \"(.*'
            r'(?P<method>'
            r'GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH'
            r').* (?P<url>.+HTTP\/1\.[10]))" (?P<statuscode>4\d{2}) '
            r'(?P<bytessent>\d+|-) (["](?P<refferer>(\-)|(.+))["]) '
            r'(["](?P<useragent>.+)["])', line)
        if request:
            urls.update({(request.group('ip'), request.group('statuscode'),
                          request.group('url')): request.group(
                'bytessent')})
    urls = OrderedDict((list(dict(sorted(urls.items(),
                                         key=lambda item: item[1],
                                         reverse=True)).items())[:number]))
    return urls
