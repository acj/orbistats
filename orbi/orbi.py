import base64
import urllib2
import re

def statistics(username, password):
    request = urllib2.Request('http://orbilogin.com/RST_statistic.htm')
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)

    response = urllib2.urlopen(request)
    html = response.read()

    js_var_pattern = re.compile(r'^var (?P<name>[A-Za-z_0-9]+?)\s*?="?(?P<value>.*?)"?;$', flags=re.MULTILINE | re.UNICODE)
    matches = re.findall(js_var_pattern, html)

    response.close()

    return {k: v for k, v in matches}
