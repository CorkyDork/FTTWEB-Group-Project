import pyrebase

service_account_email = "firebase-adminsdk-9w58e@fttweb-2fefa.iam.gserviceaccount.com"

config = {
    "apiKey": "AIzaSyAkfFcXXg4_8T2yNSoyZMYt3mEOG_SwZak",
	"authDomain": "fttweb-2fefa.firebaseapp.com",
	"databaseURL": "https://fttweb-2fefa-default-rtdb.europe-west1.firebasedatabase.app/",
	"projectId": "fttweb-2fefa",
	"storageBucket": "fttweb-2fefa.appspot.com",
	"messagingSenderId": "666615681546",
	"appId": "1:666615681546:web:81cef76f1f7117068dc5f3",
    "clientId": "666615681546-vobtmqrhfpvsb275vlthmmb2aee7ck8g.apps.googleusercontent.com",
    "clientSecret": "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",
    "service_account": {
        "email": service_account_email, 
        "private_key": {
			"type": "serviceAccount",
			"project_id": "fttweb-2fefa",
			"private_key_id": "746b6b7175c1c0488c0a26526c08d66bb80716e9",
			"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCN7/OUUfKyBNku\npHa+8w0NqW6eKVoaoZS19utkuIKJn5jvKdaagx35a2WvH8co3jZoEcqB/wViI2TE\nwGeJUTXOLD9hLSKJq+bLSmOaDd1UKc4lZDpvwHkI5Qt64N1iPB6pY0B4T+rUm7rQ\nJljD7QwKi/eXHaCuyyVDbi9tVzrCGXmHh2KCniyb72bPuS9Han+FFfOYR7p5NLGF\n6QEuR5jF4+5zs0yi0xQOQGDyxmZ9+oi29IcdW5FlhEo8M6gH8ZKBnBWq8vpy3WmO\nFf3Jig2FvQ+tip3USvw7tQ8NHr3mLh+G04QaLCRyPEilI5h87RVnD3dt7DYF3V7X\n0wPS93UjAgMBAAECggEAD+DVg3StbUvMjgK5BACFp88aAFiI62zDCZ4vVCut8r5n\nae3ow41Cd6oTjIVGDuTY+khvOp6wV/u0pKwPiRWMKt3ZU0Is2HDiF0DhppTBe05X\n8Ofm/6RtBdk1sQ/hxEEMfw+K4Uqzbwhi3DFGAdkNXUquLnoShStVplb3uEgnWxo6\nyZ12h58opaLel6UyHnq33rztLnv4mo6ZlhuJtPzAN0DAXQK2exY0NiBWPNg92k26\nXGCSQgoXQ+V1Ul4IafCfAsIb+q5xzCAVeuYfhZvYlLcylFtU6hfME74iwhgUx0wN\nQPd1/431468ffyfcPVZAjMGBax7kgdntkHm+lVvkyQKBgQDE/KyZ1GKX7u2N/RSs\nKF0j8aC4GV8gl1/ChLd7621mRrMTuZDDFRQhYpgWYJiBB9RQiT+RyNxt5/bBObNX\nYva1JN/YJ7qMcUzQuulk7rfXalIo0yNWjMC4p0GbhoGjlnj66YyzsDchBT8hagzv\nmMZRG5mHjaYgYY6tLYbvjJ8nWwKBgQC4dWgFfK2CG0/hXBYpFF99XEt9r4JFd6O6\nubZauviahFMssAGOx+mbarVj5cX04EvxQbwPM0cRQ4dzrlq3VrXeafuAygBjKWSL\nYdPNyDbs2Oyg7aVwrVpivh4zCsQKZKEZMhJIDywUq4sxT/T3upCJbEyJLaiDbrF/\nNlv2+aGb2QKBgQCkoJLTQOdhGKJZ/v9u3ZDxwDdUhIe24it6kpYRr3DPgBibTINK\nNmyLdi2qzfHGLDfpUrrY6KgoBit30vQp/SA3xWh56sICK5JKA1uZKdRk6ItfaQ1o\ngNtztvyisOfZQqE6+ULIzWVVaGAZWdsTxnc/Q7Ssz9ndyAqIersBqmE8bwKBgChy\nBeb+GYVnu7IsYOeNAgsYy6y5aRUWUJ5GzkdCq/Qlg59O0GigSQa89Rz8atVwwPYb\ndcLXeYO9jNu+pUGCD8q+7lik8kTL9LHjN2/tsK1qOyhmM1priGASU8jZWXb17aT6\np6uJOB8oJhMf9xTCoaKgTn/dtQ9snBrKrouO3PKxAoGAWwtX9oqMAq0kuuni9zG3\nq2ZLHJBYmqR+D+ImcqsvUBOLxTYJDnDrhehIL61icxvLUqni+eIqpBM4XP3/cT1X\nlAtBGjJykt1VhnOjIV0YD99vWUVw3pRdyS29SFDlXBmO87vbdg8fsXBP6yRvU5Ux\nHB5sR+PPTOdH1LspvpSJ8/0=\n-----END PRIVATE KEY-----\n",
			"client_email": "firebase-adminsdk-9w58e@fttweb-2fefa.iam.gserviceaccount.com",
			"client_id": "101782770056190409844",
			"auth_uri": "https://accounts.google.com/o/oauth2/auth",
			"token_uri": "https://oauth2.googleapis.com/token",
			"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
			"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9w58e%40fttweb-2fefa.iam.gserviceaccount.com",
		},
    },
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()