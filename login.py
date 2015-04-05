import requests


login_url = 'https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_ValLogin'

def login(data, heads, s=None):
    # create a session
    s = requests.session() if s is None else s

    s.get(login_url)

    # post the login credentials
    res = s.post(login_url,
        data=data,
        headers=heads,
    )
    print res.text
    # return the session and response
    return s, res
