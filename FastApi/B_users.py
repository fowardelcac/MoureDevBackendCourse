from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Users(BaseModel):
    id: int
    name: str
    surname: str
    age: int


user_instance = [
    Users(id=1, name="Juan", surname="Loko", age=32),
    Users(id=2, name="jjjj", surname="Loko", age=2),
    Users(id=3, name="mariano", surname="Loko", age=12),
]


@app.get("/users")
async def users():
    return user_instance


# http://localhost:8000/usersid/1
@app.get("/usersid/{id}")
async def user_id(id: int):
    return searcher_int(id)


# query
# http://localhost:8000/usersquery/?id=3
@app.get("/usersquery/")
async def user_id_v2(id: int):
    return searcher_int(id)


def searcher_int(id: int):
    # Use list comprehension to find the user with the given id

    user = next((u for u in user_instance if u.id == id), None)

    # If user is not found, raise a 404 error
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


"""
- path -> params oblig    
- query -> params que pueden no ser necesarios

"""