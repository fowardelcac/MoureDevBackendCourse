from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi everyone!"}

@app.get("/url")
async def root():
    return {"url": "www.google.com"}


