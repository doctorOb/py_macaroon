import urllib
import urllib2
import requests
import sys


login_url = 'https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_ValLogin'
registration_url = 'https://bannerweb.wpi.edu/pls/prod/bwckcoms.P_Regs'
set_term_url = 'https://bannerweb.wpi.edu/pls/prod/bwcklibs.P_StoreTerm'

#req_vals="RSTS_IN=DUMMY&assoc_term_in=DUMMY&CRN_IN=DUMMY&start_date_in=DUMMY&end_date_in=DUMMY&SUBJ=DUMMY&CRSE=DUMMY&SEC=DUMMY&LEVL=DUMMY&CRED=DUMMY&GMOD=DUMMY&TITLE=DUMMY&MESG=DUMMY&REG_BTN=DUMMY"

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
        return None

    r2 = s.post(login_url, 
        data=data,
        headers=def_headers,
    )

    if int(r2.status_code) == 403:
        return None

    return s

def set_term(term,s):
    def_headers = _headers()
    pdata = {'name_var' : 'bmenu.P_RegMnu','term_in' : term}
    r1 = s.post(set_term_url,headers=def_headers,data=pdata)
    return r1

def post_crn(term,crns, s):
    def_headers = _headers()
    pdata = {'CRN_IN' : ['DUMMY'], 
            'term_in' : term, 
            'RSTS_IN' : ['DUMMY'], 
            'assoc_term_in' : ['DUMMY',""], 
            'start_date_in' : ['DUMMY',""], 
            'end_date_in' : ['DUMMY',""],
            'SUBJ':'DUMMY',
            'CRSE':'DUMMY',
            'SEC':'DUMMY',
            'LEVL':'DUMMY',
            'CRED':'DUMMY',
            'GMOD':'DUMMY',
            'TITLE':'DUMMY',
            'MESG':'DUMMY',
            'regs_row' : 0,
            'wait_row' : 0,
            'add_row' : 10,
            'REG_BTN':['DUMMY', 'Submit Changes']}

    check = set_term(term,s)

    if int(check.status_code) != 200:
        print "error setting term {}".format(term)
        return None
    for crn in crns:
        pdata['CRN_IN'].append(crn)
        pdata['RSTS_IN'].append('RW')

    r1 = s.post(registration_url,
        headers=def_headers,data=pdata)
    
    if int(r1.status_code) != 200:
        print "Unsuccessful response from registration request"
        return None

    #TODO: better response parsing
    if "Error occurred while processing registration changes" in r1.text:
        print "Error registering CRN (server side)"
        return None

    if "DOES NOT EXIST" in r1.text:
        print "Some of the crn's given do not exist"

"""
term_in:201502
RSTS_IN:DUMMY
assoc_term_in:DUMMY
CRN_IN:DUMMY
start_date_in:DUMMY
end_date_in:DUMMY
SUBJ:DUMMY
CRSE:DUMMY
SEC:DUMMY
LEVL:DUMMY
CRED:DUMMY
GMOD:DUMMY
TITLE:DUMMY
MESG:DUMMY
REG_BTN:DUMMY
RSTS_IN:RW
CRN_IN:77222
assoc_term_in:
start_date_in:
end_date_in:
regs_row:0
wait_row:0
add_row:10
REG_BTN:Submit+Changes
"""

if __name__ == '__main__':
    creds_file = open('secrets','r')
    data = {
        'sid' : creds_file.readline()[:-1], # ignore newline
        'PIN' : creds_file.readline()[:-1]  # ignore newline
    }
    creds_file.close()
    session = post_login(data)
    if session is None:
        print("failed to login, try again")
        sys.exit(1)
    post_crn('201502',['12345'],session)
