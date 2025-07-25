import requests
import data
import jwt


class session:
    def __init__(self):
        self.session = requests.session()
        self.phoneNumber = None
        self.password = None
        self.token = None
        self.authExpirey = None 

    
    
    def Authenticate(self):
        #todo add checks to see if inputs are valid
        #todo once all inputs are valid check if there is a token already present
        #todo if token is present check if its expired and then valid or not then update accordingly
        #todo send false when auth failed or throw an exception
        post=f'{{"msisdn":"{self.phoneNumber}","password":"{self.password}"}}'
        headers = {"version": "0.13.0"}
        req = requests.Request('POST',data.static.loginUrl(),data=post,headers=headers)
        req = req.prepare()
        res = self.session.send(req)
        self.token = res.json()["data"][0]["accessToken"]
        self.authExpirey = jwt.decode(self.token,options={"verify_signature": False})["expireAt"]
        return True


    def isAuthenticated(self) -> bool:
        headers = {"version": "0.13.0"}
        headers["Authorization"] = f"Bearer {self.token}"
        req = requests.Request('POST',data.static.verifyAuth(),headers=headers)
        req = req.prepare()
        res = self.session.send(req)
        if (res.status_code==200):
            #success
            #todo figure out if this fucntion updates the token or not then update current token accordingly
            #self.token = res.json()["data"][0]["accessToken"]
            #self.authExpirey = jwt.decode(self.token,options={"verify_signature": False})["expireAt"]
            return True
        else:
            #failed
            return False




