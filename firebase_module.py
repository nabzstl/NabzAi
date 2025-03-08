import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    cred = credentials.Certificate('firebase-adminsdk.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nabzai-default-rtdb.firebaseio.com'
    })

def save_user_feedback(user_id, feedback):
    ref = db.reference(f'/feedback/{user_id}')
    ref.push(feedback)

def get_user_feedback(user_id):
    ref = db.reference(f'/feedback/{user_id}')
    return ref.get()
