import urllib
import urllib2
import requests
import mechanize


login_url = 'https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_ValLogin'
registration_url = 'https://bannerweb.wpi.edu/pls/prod/bwskfreg.P_AltPin'

def old_post_login():

	req = urllib2.Request(login_url, data, )

def post_login():
	s = requests.Session()
    f = str(raw_input("What is the name of the file with your WPI username and password?\n"))
    creds_file = open(f,'r')
    data['sid'] = creds_file.readline()[:-1] # ignore newline
    data['PIN'] = creds_file.readline()[:-1] # ignore newline
	response = s.get(login_url,
		headers={'User-Agent' : 'curl/7.30.0',
				 'Host' : 'bannerweb.wpi.edu',
				 'Accept' : '*/*'}
	)

	cookies = response.cookies

	response = s.post(login_url, 
		data=data, 
		headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'},
		cookies=cookies
	)
	#print response.text.encode('ascii','ignore')
	print response.status_code
	print response.headers
	return s

if __name__ == '__main__':
	post_login()
