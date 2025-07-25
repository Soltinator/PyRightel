
class static:
    #all of the static data of the wrapper is stored here
    #todo find a way to store these in a file and read from it properly
    globalHeaders = {"version": "0.13.0"} 
    rootUrl = "https://myrightel-api.rightel.ir" 
    endpoints = {
        #todo add all of the endpoints to this dict
        "login":"/v2/auth/login/password/",
        "verifyAuth":"/v2/auth/"
    } 

    #todo find a better way to serve read only strings

    def loginUrl():
        return static.rootUrl+static.endpoints["login"]

    def verifyAuth():
        return static.rootUrl+static.endpoints["verifyAuth"]