from datetime import datetime, timedelta
import pytz
from pymongo import MongoClient
from bson import ObjectId



def current_time():

    # Get the current UTC time
    utc_now = datetime.utcnow()

    # Define the Indian Standard Time (IST) timezone
    ist_timezone = pytz.timezone('Asia/Kolkata')

    # Convert UTC time to IST
    ist_now = utc_now + timedelta(hours=5, minutes=30)
    ist_now = ist_timezone.localize(ist_now)

    # Format the datetime as a string
    return ist_now.strftime('%Y-%m-%d %H:%M:%S')


def insert_one(post):
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://vishwanath:vishwanath@vishwanath.zs8kw.mongodb.net/secure_iot?retryWrites=true&w=majority')

    # Access a database
    db = client['secure_iot']

    # Access a collection (similar to a table in relational databases)
    collection = db['iot_rest']

    post['Timestamp'] = current_time()

    collection.insert_one(post)
    
    # Close the connection
    client.close()
    
    
    
def read_documents(query={}):
    client = MongoClient('mongodb+srv://vishwanath:vishwanath@vishwanath.zs8kw.mongodb.net/secure_iot?retryWrites=true&w=majority')

    # Access a database
    db = client['secure_iot']

    # Access a collection (similar to a table in relational databases)
    collection = db['iot_rest']

    documents = list(collection.find(query))
    client.close()

    results = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        results.append(doc)

    return results

def update_document(document_id, update_values):
    
    # Define the query based on time
    client = MongoClient('mongodb+srv://vishwanath:vishwanath@vishwanath.zs8kw.mongodb.net/secure_iot?retryWrites=true&w=majority')

    # Access a database
    db = client['secure_iot']

    # Access a collection (similar to a table in relational databases)
    collection = db['iot_rest']

    # Define the query based on the document_id
    query = {'_id': ObjectId(document_id)}

    # Update the document based on the query
    result = collection.update_one(query, {'$set': update_values})

    client.close()
    
    return result.modified_count
