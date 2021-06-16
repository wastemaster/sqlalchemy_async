import os
from databases import Database
from dotenv import load_dotenv
import sqlalchemy

db = Database(os.environ["DATABASE_URL"])
metadata = sqlalchemy.MetaData()
