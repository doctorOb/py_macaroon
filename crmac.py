import sys

from login import login
from post_crns import post_crns


def _headers():
	"""return a default list of headers for use in all requests. Some / all of these might not be necessary"""
	return {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36', #pretend I'm a browser
		'Host' : 'bannerweb.wpi.edu',
		'Accept' : '*/*'
	}



if __name__ == '__main__':
    creds_file = open('secrets','r')
    data = {
        'sid' : creds_file.readline()[:-1], # ignore newline
        'PIN' : creds_file.readline()[:-1]  # ignore newline
    }
    creds_file.close()
    session, response = login(data, _headers())
    while response.status_code != 200:
        session, response = login(data, _headers())
    post_crns(session, _headers())
