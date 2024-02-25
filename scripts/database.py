from pymongo import MongoClient 

def setup_database():
    """Setup the database connection for the application using the MongoClient from pymongo.
    Args:
        None
    Returns:
        db: The database object
        mongo: The MongoClient object
    """
    
    mongo = MongoClient()
    db = mongo.mydb
    return db, mongo
