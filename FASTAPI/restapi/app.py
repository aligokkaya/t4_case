from fastapi import FastAPI
from crud.main import t
import uvicorn
app = FastAPI()

app.include_router(t)

if __name__ == "__main__":
    uvicorn.run(app)    
    