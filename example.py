from PyRightel import main as Rightel
import pickle
import os.path

phoneNumber = "09876543210"
password = "**********"

session = None

#saving the authentication session into a file as a simple cache (proper chacing will be a part of the wrapper)
if (os.path.isfile('session.temp')):
    with open('session.temp', 'rb') as handle:
        session = pickle.load(handle)
else:
    session = Rightel.getSession(phoneNumber,password)
    with open('session.temp', 'wb') as handle:
        pickle.dump(session, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"is authenticated: {Rightel.isAuthenticated(session)}\n")

print("Here is a list of active packages and their remaining:")
ls = Rightel.listPackages(session)
for package in ls:
    print(f"Package Type: {str(package.packageType)} - remain: {package.remain}")