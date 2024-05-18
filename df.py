import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
i=True
# Use a service account.

cred = credentials.Certificate('serviceAccountKey.json')
if not firebase_admin._apps:
    app = firebase_admin.initialize_app(cred)
else:
    app = firebase_admin.get_app()    
db = firestore.client()
    

# Get data from a Firestore collection
users = db.collection('Peliculas').stream()
# Convert data to a list of dictionaries
users_data = [doc.to_dict() for doc in users]
# Create DataFrame
df = pd.DataFrame(users_data)

print(df)