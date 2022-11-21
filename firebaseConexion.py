import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# se carga el certificado
firebase_sdk = credentials.Certificate("./firebase-config.json")

# se hace referencia a la base de datos en tiempo real
firebase_admin.initialize_app(firebase_sdk, { "databaseURL": "https://touchpet-a24e7-default-rtdb.firebaseio.com"})

database = db