from fastapi import FastAPI 
app = FastAPI()
@app.get("/") 
async def index(): 
    return "Hello World!" 
@app.get("/test") 
async def test(): return "test"