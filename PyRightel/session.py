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
        if (self.token == None or not isAuthenticated(self)):

            if (type(self.phoneNumber) is str and type(self.password) is str):
                if ((len(self.phoneNumber)>=9 and len(self.phoneNumber)<=13)or(len(self.password)>=8 and en(self.password)<=12)):
                    if(self.phoneNumber.isnumeric()):
                            
                        post=f'{{"msisdn":"{self.phoneNumber}","password":"{self.password}"}}'
                        headers = {"version": "0.13.0"}
                        req = requests.Request('POST',data.static.loginUrl(),data=post,headers=headers)
                        req = req.prepare()
                        res = self.session.send(req)
                        if (res.status_code == 200):
                            self.token = res.json()["data"][0]["accessToken"]
                            self.authExpirey = jwt.decode(self.token,options={"verify_signature": False})["expireAt"]
                            return True
                        elif (res.status_code == 401):
                            #bad login creds
                            raise authException(f"invalid login, check phone number or password\nResponse: {res.reason}-({res.status_code})\n{res.url}")
                            return False
                        elif (res.status_code != 200 and res.status_code != 401):
                            raise authException(f"unexpected status while authenticating, is Rightel service available?\nResponse: {res.reason}-({res.status_code})\n{res.url}")
                            return None
                        else:
                            raise authException(f"unknown error while authenticating, check internet connection perhaps?\nResponse: {res.reason}-({res.status_code})\n{res.url}")
                            return None

                    elif(not self.phoneNumber.isnumeric()):
                        raise authException("phone number has invalid characters")
                        return None

                elif (len(self.phoneNumber)<9 or len(self.phoneNumber)>13):
                    raise authException("phone number has invalid length")
                    return None

                elif (len(self.password)<8 or en(self.password)>12):
                    raise authException("password has invalid length")
                    return None

                elif ((len(self.password)<8 or en(self.password)>12) and (len(self.phoneNumber)<9 or len(self.phoneNumber)>13)):
                    raise authException("phone number and password are a valid lenght")
                    return None

            elif (type(self.phoneNumber) is not str):
                raise authException("phone number is not a string")

            elif (type(self.password) is not str):
                raise authException("password is not a string")

            elif (type(self.phoneNumber) is not str and type(self.password) is not str):
                raise authException("phone number and password are not a string, have you forgotten setting them?")

        else:
            return isAuthenticated(self)




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




