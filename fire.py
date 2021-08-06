
import pyrebase
from time import sleep
import random
import sys 
config = {     
  "apiKey": "UaNnD4O1nSuvv1k55vSxq46pJSwJBJXzbQKzRgQq",
  "authDomain": "home2-9fb78.firebaseapp.com",
  "databaseURL": "https://home2-9fb78-default-rtdb.firebaseio.com/",
  "storageBucket": "home2-9fb78.appspot.com"
}

firebase = pyrebase.initialize_app(config)  

try:
    while True:

        database = firebase.database()
        Prod1val = database.child("Prod1").get().val() # To get value from firebase database
        print(Prod1val)
        database.child("Prod2").set(random.randint(2,9)) # To set value to firebase database
        sleep(5)
        

       
except KeyboardInterrupt:
    sys.exit()
    