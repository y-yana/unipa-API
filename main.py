from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from scraping import scraping


app = FastAPI()


# リクエストbodyを定義
class User(BaseModel):
    url: Optional[str] = None
    user_id: str
    user_password: str
    show_chrome:  Optional[bool] = None


# シンプルなJSON Bodyの受け取り
@app.post("/user/")
def create_user(user: User):
    #ans = scraping.rename(user.user_id)
    if user.url == None:
        user.url = 'https://hiro-unipa.itp.kindai.ac.jp/up/faces/up/po/Poa00601A.jsp'
    if user.show_chrome == None:
        user.show_chrome = False
    ans = scraping.main(user.url, user.user_id, user.user_password, user.show_chrome)
    return ans
    #return {"res": "ok", "ID": user.user_id, "password": user.user_password}
