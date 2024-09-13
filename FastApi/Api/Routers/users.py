from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router_user = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"msg": "no encontrado"}}
)


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


@router_user.get("/")
async def users():
    return user_instance


@router_user.get("/{id}")
async def user_id(id: int):
    user = searcher_int(id)
    if user:
        return user_instance[id-1]


@router_user.post("/", status_code=201)
async def user(user: Users):
    if not searcher_int(user.id):
        user_instance.append(user)
        return user
    else:
        raise HTTPException(status_code=204, detail="ya existe")


@router_user.put("/")
async def user(user: Users):
    found = False
    for index, i in enumerate(user_instance):
        if i.id == user.id:
            user_instance[index] = user
            found = True
    if not found:
        return {"error": "there is an error dude"}


# http://localhost:8000/users/1
@router_user.delete("/{id}")
async def user(id: int):
    found = False
    for index, i in enumerate(user_instance):
        if i.id == id:
            del user_instance[index]
            found = True
    if not found:
        return {"error": "there is an error dude"}


def searcher_int(id: int):
    return any(user.id == id for user in user_instance)
