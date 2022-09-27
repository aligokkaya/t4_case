from curses import echo
from sqlalchemy import create_engine,MetaData

meta = MetaData()
db_engine = create_engine("mysql+pymysql://root:Challenge_t4@164.92.161.222/t4_challenge")
conn = db_engine.connect()
   

