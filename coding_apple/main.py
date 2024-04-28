from fastapi import FastAPI
from fastapi.responses import FileResponse
# DB 접속

app = FastAPI()

from pydantic import BaseModel
class Model(BaseModel):
  name : str
  phone : int

@app.post("/send")
def 작명(data : Model):
  print(data)
  # DB 적재
  # async 함수 사용 시 await으로 비동기 처리 가능
  return '전송완료'

@app.get("/")
def 작명():
  return FileResponse("index.html")

# @app.post("/send")
# def 작명():
#   return '전송완료'

@app.get("/data")
def 작명():
  return {"hello" : 1234}

# uvicorn main:app --reload --host=0.0.0.0 --port=8000