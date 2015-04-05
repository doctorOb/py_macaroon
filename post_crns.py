import requests
import sys

registration_url = 'https://bannerweb.wpi.edu/pls/prod/bwckcoms.P_Regs'


def register_crns(crns, session, heads):
    for k in crns.keys():
        data = {
            'RSTS_IN' : [],
            'CRN_IN' : [],
            'term_in' : k,
            # they need all this dummy data for some reason
            'ASSOC_TERM_IN' : 'DUMMY',
            'START_DATE_IN' : 'DUMMY',
            'END_DATE_IN' : 'DUMMY',
            'SUBJ' : 'DUMMY',
            'CRSE' : 'DUMMY',
            'SEC' : 'DUMMY',
            'LEVL' : 'DUMMY',
            'CRED' : 'DUMMY',
            'GMOD' : 'DUMMY',
            'TITLE' : 'DUMMY',
            'MESG' : 'DUMMY',
            'REG_BTN' : 'DUMMY',
            'REGS_ROW' : '0',
            'WAIT_ROW' : '0',
            'ADD_ROW' : '10'
        }
        for crn in crns[k]:
            data['CRN_IN'].append(crn)
            data['RSTS_IN'].append('RW')
        print data
        r = session.post(
                registration_url,
                data=data,
                headers=heads
                )
        if r.status_code != 200:
            print "something went wrong when trying to register for term:", k
        print r.text


def post_crns(session, heads):
    # open the CRNS file
    with open('crns', 'r') as f:
        # an array of CRNS for a single term
        crns_with_terms = {}
        # for each line
        for line in f:
            # if it starts with "[TERM]"
            if line.startswith("[TERM]"):
                # the name of the term itself
                term = line.replace("[TERM]", "")[:-1]
                # map the term to an empty array of CRNS
                crns_with_terms[term] = []
            else:
                # append the CRN to the term's CRN array
                crns_with_terms[term].append(line[:-1])
        # register the CRNS
        register_crns(crns_with_terms, session, heads)
