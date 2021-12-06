import urllib.request
from urllib.error import URLError, HTTPError


class Request():

    def html_in_page(self, url):
        try:
            request_response = urllib.request.urlopen(url, timeout=20)
        except HTTPError as e:
            # do something
            print('Error code: ', e.code)
            return None
        except URLError as e:
            # do something
            print('Reason: ', e.reason)
            return None
        return str(request_response.read())
