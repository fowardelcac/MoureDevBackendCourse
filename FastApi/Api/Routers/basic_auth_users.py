from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="Login")


class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool


class UserDb(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "fullname": "hola juan",
        "email": "juanucudcjis@gmail.com",
        "disabled": False,
        "password": "yosoyelleon",
    },
    "mouredev1": {
        "username": "mouredev1",
        "fullname": "hola juan1",
        "email": "juanucudcji11s@gmail.com",
        "disabled": True,
        "password": "yosoyelleon",
    },
}


def search_user(username: str):
    if username in users_db:
        return UserDb(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autorizado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="usuario no encontrado")

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contsrae;a esta mal")
    return {"acces_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
