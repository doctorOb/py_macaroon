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
	data = {  'sid' : 'drob',
			  'PIN' : 'yuBfx2020'}
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

def br_em():
	br = mechanize.Browser()
	br.open("https://bannerweb.wpi.edu")
	br.select_form(name="loginform")
	br["sid"] = "drob"
	br["PIN"] = "yuBfx2020"
	resp = br.submit()
	print resp.info()
	resp = br.open(registration_url)
	#print resp.read()
	br["term_in"] = "201502"
	resp = br.submit()
	print resp.read()

if __name__ == '__main__':
	post_login()
