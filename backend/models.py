from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    username = Column(String)
    rating = Column(Integer)
    review = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())