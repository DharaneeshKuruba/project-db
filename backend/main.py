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

@app.get("/reviews/{hotel_id}")
def get_reviews(hotel_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(
        models.Review.hotel_id == hotel_id
    ).all()

    return reviews


@app.get("/hotels")
def get_hotels(db: Session = Depends(get_db)):
    return db.query(models.Hotel).all()