from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: Optional[int] = None
    username: str
    age: int


@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})


@app.post("/user/", response_model=User)
async def post_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return f"User {user.id} is registered"


@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User) -> str:
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = user
    return f"User {user_id} was updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")

    users.pop(user_id)
    return f"User {user_id} was deleted"
