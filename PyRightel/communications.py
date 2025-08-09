import requests
from . import data
import jwt
import logging

log = logging.getLogger('PyRightel.data')
log.debug("setting up communications module")

#allowed methods
#POST, OPTIONS, GET, PUT, DELETE

#used methods
#POST, GET, PUT


#TODO proper error handeling both in network errors and response errors from api
def get(session,endpoint)->dict:
    req = requests.Request('GET',endpoint,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req)
    return res

def post(session,endpoint,postData)->dict:
    req = requests.Request('POST',endpoint,data=postData,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req)
    return res

def put(session,endpoint,putData)->dict:
    req = requests.Request('PUT',endpoint,data=putData,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req)
    return res

log.debug("finished setting up communications module")