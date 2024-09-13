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


@app.get("/users/")
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
    return any(user.id == id for user in user_instance)


"""
- path -> params oblig    
- query -> params que pueden no ser necesarios

"""


@app.post("/user/", status_code=201)
async def user(user: Users):
    if not searcher_int(user.id):
        user_instance.append(user)
        return user
    else:
        raise HTTPException(status_code=204, detail="ya existe")


@app.put("/user/")
async def user(user: Users):
    found = False
    for index, i in enumerate(user_instance):
        if i.id == user.id:
            user_instance[index] = user
            found = True
    if not found:
        return {"error": "there is an error dude"}


# http://localhost:8000/users/1
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, i in enumerate(user_instance):
        if i.id == id:
            del user_instance[index]
            found = True
    if not found:
        return {"error": "there is an error dude"}
