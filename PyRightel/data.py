from dataclasses import dataclass


class Endpoint(property):
    def __init__(self,getter):
        self.getter = getter
    def __get__(self,cls,owner):
        return self.getter(owner)

class static:
    #all of the static data of the wrapper is stored here
    #todo find a way to store these in a file and read from it properly
    globalHeaders = {"version": "0.13.0"} 
    rootUrl = "https://myrightel-api.rightel.ir" 
    endpointsList = {
        #todo add all of the endpoints to this dict
        "PasswordLogin":"/v2/auth/login/password/",
        "verifyToken":"/v2/auth/"
    } 

    pyrVersion = "0.0.1-pa"
    apiVersion = "0.13.0"
    userAgent = f"PyRightel/{pyrVersion}"

    #todo find a way to make these read only and not mutable (i hate python)
    #todo this seems inefficent, cache or static? find a way to serve a premade list instead of adding strings for each read (but for now it works fine)
    class endpoints:
        @Endpoint
        def LoginUsingPassword(self):
            return static.rootUrl+static.endpointsList["PasswordLogin"]

        @Endpoint
        def verifyToken(self):
            return static.rootUrl+static.endpointsList["verifyToken"]