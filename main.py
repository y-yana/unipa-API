from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# リクエストbodyを定義
class User(BaseModel):
    user_id: str
    user_password: str


# シンプルなJSON Bodyの受け取り
@app.post("/user/")
def create_user(user: User):
    return {"res": "ok", "ID": user.user_id, "password": user.user_password}
