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

    #possible errors by this point: 
    #invalid session object, invalid endpoint
    #endpoint should be string
    #session should have a token and not be expired

    # when requests.HTTPError /(means that the response was not 200)
    # log into console 
    # return error status or null

    #when 
    # requests.ConnectTimeout 
    # requests.ConnectionError
    # requests.ReadTimeout
    # requests.Timeout
    # should be handled by urllib3 and retry strategy in data.static

    #when requests.RequestException it was unknown error and should dump all and abort excution

    # as for these i dont know what to do yet. 
    # requests.TooManyRedirects
    # requests.JSONDecodeError
    # soft fail maybe? (not abort but return null data or error data)
    
    #TODO error check for json parsing

    req = requests.Request('GET',endpoint,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req,timeout=data.static.requestTimeout)
    if (res.status_code == 200):
        #check if the json data is ok here
        outdata = res.json()["data"]

    return data.response(data.responseStatus["ok"],outdata)

def post(session,endpoint,postData)->dict:
    req = requests.Request('POST',endpoint,data=postData,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req,timeout=data.static.requestTimeout)
    return res

def put(session,endpoint,putData)->dict:
    req = requests.Request('PUT',endpoint,data=putData,headers=session.headers)
    req = req.prepare()
    res = session.session.send(req,timeout=data.static.requestTimeout)
    return res

log.debug("finished setting up communications module")