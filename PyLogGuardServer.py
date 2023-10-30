from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import sqlite3

app = FastAPI()

APIDB = 'APIDatabase.db'    # Database file name

conn = sqlite3.connect(APIDB, check_same_thread=False)
cursor = conn.cursor()

#Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        date INTEGER,
        device TEXT,
        type TEXT,
        msg TEXT,
        id integer PRIMARY KEY AUTOINCREMENT
    )
''')
conn.commit()

#check if database works:
# qry = "insert into logs (date, device, type, msg) values ('6/6/6666', 'TEST_Server', 'Test_Device', 'Test_Msg');"
# cursor.execute(qry)
# conn.commit()

class Log(BaseModel):
    date : str
    device : str
    type : str
    msg : str

    
    def __init__(self, date: str, device: str,type : str, msg: str, **data):
        super().__init__(date=date, device=device, type=type, msg=msg, **data)



@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/all")    # returns whole database, only for testing purposes
def read_all():
    cursor.execute("SELECT * FROM logs")
    return cursor.fetchall()
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
