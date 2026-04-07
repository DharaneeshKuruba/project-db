from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

from pydantic import BaseModel

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class ReviewCreate(BaseModel):
    hotel_id: int
    username:str
    rating: int
    review:str
    
@app.post("/reviews")
def create_review(data: ReviewCreate, db: Session = Depends(get_db)):
    new_review=models.Review(
        hotel_id=data.hotel_id,
        username=data.username,
        rating=data.rating,
        review=data.review
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)