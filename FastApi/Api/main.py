from fastapi import FastAPI
from Routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(products.router_prods)
app.include_router(users.router_user)
#http://localhost:8000/statics/images/image.png
app.mount("/statics", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hi everyone!"}


@app.get("/url")
async def root():
    return {"url": "www.google.com"}
