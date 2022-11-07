import firebase_admin
from firebase_admin import db
from random_username.generate import generate_username

cred_obj = firebase_admin.credentials.Certificate('cyber-security-project-9d147-firebase-adminsdk-kohge-efdf8dfb2a.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://cyber-security-project-9d147-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference("/accounts")

passwords = ["123456", "12345", "123456789", "password", "iloveyou", "princess", "1234567", "rockyou", 
    "12345678", "abc123", "nicole", "daniel", "654321", "michael", "ashley","qwerty", "m385hBz#sCiXzLf*", "8#nJ7hH7o@E8bpFK",
    "ckh!WpqUv8rRVNr", "VKpLwpdfB98J*&g7", "pnprp4UWim#$SJoM", "S#kiVRnS4yc8H3"]

usernames = generate_username(len(passwords))
for i in range(len(passwords)):
    ref.push({"email": usernames[i] + "@rockyou.com", "password": passwords[i]})