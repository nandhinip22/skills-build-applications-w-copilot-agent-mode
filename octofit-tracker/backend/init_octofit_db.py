from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['octofit_db']

# Create collections
collections = ['users', 'teams', 'activities', 'workouts', 'leaderboard']
for col in collections:
    if col not in db.list_collection_names():
        db.create_collection(col)

# Ensure unique index on email for users
try:
    db.users.create_index('email', unique=True)
except Exception as e:
    print('Index creation error:', e)

print('Collections and index created successfully.')

# Diagnostic: List collections and show sample documents
print('Collections:', db.list_collection_names())
for col in collections:
    print(f'Sample from {col}:', db[col].find_one())