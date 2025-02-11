from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import chatbot_response


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running!"}

@app.get("/query/")
def get_product_info(query: str, db: Session = Depends(get_db)):
    return {"response": chatbot_response(query, db)}
