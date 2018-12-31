import requests

class GetRequests:
    def run_url(self, url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        r = requests.get(url,headers = headers)
        return r
