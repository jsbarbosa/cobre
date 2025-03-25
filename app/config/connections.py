from .settings import DATABASE_URI
from sqlalchemy import create_engine


def get_connection():
    return create_engine(DATABASE_URI).connect()
    
