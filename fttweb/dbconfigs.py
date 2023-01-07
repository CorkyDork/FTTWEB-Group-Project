import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth



config = {
    "apiKey": "AIzaSyDiSiQcmuTEHdHUio2tOprPOX65MJ8SkMk",
	"authDomain": "test-4d090.firebaseapp.com",
	"databaseURL": "https://test-4d090-default-rtdb.firebaseio.com",
	"projectId": "test-4d090",
	"storageBucket": "test-4d090.appspot.com",
	"messagingSenderId": "1060349065580",
	"appId": "1:1060349065580:web:1ee1a40ea145f1ef9a5b49",
	"measurementId": "G-05JYEHXSQQ",
	"clientId": "1060349065580-jhrpkthkjcqi84nbjfkspmvhi0kqi1ko.apps.googleusercontent.com",
    "clientSecret": "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",

	
}


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
RTDb = firebase.database() # real time database

# Use a service account.
cred = credentials.Certificate('fttweb/firebase.json')
app = firebase_admin.initialize_app(cred)
FSDb = firestore.client() # Firestore database