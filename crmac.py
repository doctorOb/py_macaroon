import urllib
import urllib2
import requests


login_url = 'https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_ValLogin'
registration_url = 'https://bannerweb.wpi.edu/pls/prod/bwskfreg.P_AltPin'

def old_post_login():

	req = urllib2.Request(login_url, data, )

def _headers():
	"""return a default list of headers for use in all requests. Some / all of these might not be necessary"""
	return {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36', #pretend I'm a browser
		'Host' : 'bannerweb.wpi.edu', 
		'Accept' : '*/*'
	}


def post_login(data, s=None):
    s = requests.session() if s is None else s
    def_headers = _headers()
    r1 = s.get(login_url,
        headers=def_headers
    )

    if int(r1.status_code) == 403:
        return post_login(data, s)

    r2 = s.post(login_url, 
        data=data,
        headers=def_headers,
    )

    if int(r2.status_code) == 403:
        return post_login(data, s)
    print r2.status_code
    return s

if __name__ == '__main__':
    creds_file = open('secrets','r')
    data = {
        'PIN' : creds_file.readline()[:-1], # ignore newline
        'sid' : creds_file.readline()[:-1]  # ignore newline
    }
    creds_file.close()
    session = post_login(data)
    crns = {
    
    }
    post_crn(
