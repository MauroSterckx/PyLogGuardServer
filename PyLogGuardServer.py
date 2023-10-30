from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
